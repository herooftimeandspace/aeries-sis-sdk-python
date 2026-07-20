"""Tests for bounded response reads and credential-safe failure context."""

from __future__ import annotations

import json

import httpx
import pytest

from aeries_sis_sdk import AsyncClient, Client
from aeries_sis_sdk.errors import AeriesResponseTooLargeError, AeriesValidationError


def student_picture_body(raw_binary: str = "cGhvdG8=") -> bytes:
    """Build a realistic compact student-picture response as encoded JSON bytes."""

    return json.dumps(
        {
            "StudentID": "99400001",
            "Pictures": [
                {
                    "SchoolYear": 2024,
                    "RawBinary": raw_binary,
                    "FileExtension": "jpg",
                    "FileSize": 5,
                }
            ],
            "SchoolCode": 994,
        },
        separators=(",", ":"),
    ).encode()


def test_sync_picture_response_below_and_exactly_at_limit() -> None:
    """The sync client should accept realistic picture JSON through the exact byte limit."""

    body = student_picture_body()

    def handler(request: httpx.Request) -> httpx.Response:
        """Return the same picture body for both boundary checks."""

        return httpx.Response(200, request=request, content=body)

    for limit in (len(body) + 1, len(body)):
        with Client(
            base_url="https://district.example.edu/aeries",
            certificate="secret",
            max_response_bytes=limit,
            transport=httpx.MockTransport(handler),
        ) as client:
            result = client.students.get_student_picture(school_code=994, student_id=99400001)
        assert result.student_id == "99400001"


def test_sync_oversized_picture_is_not_retried_or_retained() -> None:
    """A known oversized picture should fail once without storing its partial bytes."""

    body = student_picture_body("cGhvdG8=" * 20)
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        """Count requests so an accidental retry is observable."""

        nonlocal attempts
        attempts += 1
        return httpx.Response(200, request=request, content=body)

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(body) - 1,
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesResponseTooLargeError) as raised:
        client.students.get_student_picture(school_code=994, student_id=99400001)

    assert attempts == 1
    assert raised.value.context is not None
    assert raised.value.context.path == (
        "/api/v5/schools/{SchoolCode}/StudentPictures/{StudentID}"
    )
    assert body.decode() not in repr(raised.value)
    assert not hasattr(raised.value, "response_body")


def test_sync_oversized_error_uses_typed_size_error() -> None:
    """An oversized provider error should fail before its body is parsed or retained."""

    body = json.dumps({"Message": "provider detail " * 40}).encode()

    def handler(request: httpx.Request) -> httpx.Response:
        """Return a non-retryable oversized validation error."""

        return httpx.Response(400, request=request, content=body)

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(body) - 1,
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesResponseTooLargeError):
        client.students.get_student_picture(school_code=994, student_id=99400001)


def test_sync_error_context_omits_query_credentials_and_unsafe_detail() -> None:
    """Exception rendering should not expose query data, certificates, or provider URLs."""

    certificate = "reusable-certificate-value"
    unsafe_message = (
        f"Credential {certificate}\nsee https://example.invalid/path?token=raw-photo-data"
    )

    def handler(request: httpx.Request) -> httpx.Response:
        """Return an error containing values that are unsafe to preserve."""

        return httpx.Response(400, request=request, json={"Message": unsafe_message})

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate=certificate,
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.request("GET", "/students", params={"token": "query-secret"})

    rendered = f"{raised.value!s} {raised.value.context!r}"
    assert certificate not in rendered
    assert "query-secret" not in rendered
    assert "raw-photo-data" not in rendered
    assert raised.value.context is not None
    assert raised.value.context.path == "/students"
    assert raised.value.context.detail is None


def test_safe_provider_detail_is_normalized_and_bounded() -> None:
    """Safe provider text should remain useful but never exceed its documented bound."""

    detail = "Temporary\nvalidation failure " + ("x " * 400)

    def handler(request: httpx.Request) -> httpx.Response:
        """Return a long but otherwise safe provider message."""

        return httpx.Response(400, request=request, json={"Message": detail})

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.request("GET", "/students")

    assert raised.value.context is not None
    assert raised.value.context.detail is not None
    assert "\n" not in raised.value.context.detail
    assert len(raised.value.context.detail) == 512
    assert str(raised.value) == raised.value.context.detail


@pytest.mark.parametrize("invalid_limit", [0, -1, 1.5, True])
def test_sync_client_rejects_invalid_response_limits(invalid_limit: object) -> None:
    """The sync constructor should reject non-positive and non-integer limits."""

    with pytest.raises((TypeError, ValueError)):
        Client(
            base_url="https://district.example.edu/aeries",
            certificate="secret",
            max_response_bytes=invalid_limit,  # type: ignore[arg-type]
        )


@pytest.mark.asyncio
async def test_async_picture_response_at_limit_and_oversized() -> None:
    """The async client should share the sync client's exact boundary behavior."""

    body = student_picture_body()

    def handler(request: httpx.Request) -> httpx.Response:
        """Return one picture response through the async mock transport."""

        return httpx.Response(200, request=request, content=body)

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(body),
        transport=httpx.MockTransport(handler),
    ) as client:
        result = await client.students.get_student_picture(
            school_code=994, student_id=99400001
        )
    assert result.student_id == "99400001"

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(body) - 1,
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(AeriesResponseTooLargeError):
            await client.students.get_student_picture(school_code=994, student_id=99400001)


@pytest.mark.asyncio
async def test_async_oversized_error_and_malformed_json() -> None:
    """The async client should bound errors and still type malformed JSON failures."""

    oversized_body = json.dumps({"Message": "provider detail " * 40}).encode()

    def oversized_handler(request: httpx.Request) -> httpx.Response:
        """Return an oversized non-retryable HTTP error."""

        return httpx.Response(400, request=request, content=oversized_body)

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(oversized_body) - 1,
        transport=httpx.MockTransport(oversized_handler),
    ) as client:
        with pytest.raises(AeriesResponseTooLargeError):
            await client.students.get_student_picture(school_code=994, student_id=99400001)

    def malformed_handler(request: httpx.Request) -> httpx.Response:
        """Return a bounded body that is not JSON."""

        return httpx.Response(200, request=request, content=b"not-json")

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=64,
        transport=httpx.MockTransport(malformed_handler),
    ) as client:
        with pytest.raises(AeriesValidationError):
            await client.students.get_student_picture(school_code=994, student_id=99400001)
