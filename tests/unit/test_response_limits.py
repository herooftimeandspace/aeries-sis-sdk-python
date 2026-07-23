"""Tests for bounded response reads and credential-safe failure context."""

from __future__ import annotations

import json

import httpx
import pytest

from aeries_sis_sdk import AsyncClient, Client
from aeries_sis_sdk._runtime import read_limited_response, read_limited_response_async
from aeries_sis_sdk.errors import (
    AeriesResponseTooLargeError,
    AeriesTransportError,
    AeriesValidationError,
)


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


def test_sync_oversized_retryable_error_is_not_retried() -> None:
    """A retryable status with an oversized body should fail on the first response."""

    body = json.dumps({"Message": "retry later " * 40}).encode()
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        """Return an oversized 503 before a success that must never be requested."""

        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(503, request=request, content=body)
        return httpx.Response(200, request=request, json={"AeriesVersion": "1.0"})

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(body) - 1,
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesResponseTooLargeError):
        client.system.get_aeries_installation_information()

    assert attempts == 1


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


def test_provider_detail_omits_actual_query_and_header_secrets() -> None:
    """Provider text echoing per-request query or header values should be discarded."""

    query_secret = "per-request-query-secret"
    header_secret = "per-request-certificate"

    def handler(request: httpx.Request) -> httpx.Response:
        """Echo actual request values without URL punctuation or long encoded data."""

        message = f"Rejected {request.url.params['token']} and {request.headers['AERIES-CERT']}"
        return httpx.Response(400, request=request, json={"Message": message})

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="constructor-certificate",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.request(
            "GET",
            "/students",
            params={"token": query_secret},
            headers={"AERIES-CERT": header_secret},
        )

    rendered = f"{raised.value!s} {raised.value.context!r}"
    assert query_secret not in rendered
    assert header_secret not in rendered
    assert raised.value.context is not None
    assert raised.value.context.detail is None


def test_provider_detail_omits_generated_path_identifiers() -> None:
    """Provider text should not reintroduce identifiers removed by contract paths."""

    student_id = "99400001"

    def handler(request: httpx.Request) -> httpx.Response:
        """Echo the generated operation's student identifier without URL syntax."""

        return httpx.Response(
            400,
            request=request,
            json={"Message": f"Student {student_id} was not found"},
        )

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.students.get_student_picture(school_code=994, student_id=student_id)

    rendered = f"{raised.value!s} {raised.value.context!r}"
    assert student_id not in rendered
    assert raised.value.context is not None
    assert raised.value.context.path == (
        "/api/v5/schools/{SchoolCode}/StudentPictures/{StudentID}"
    )


def test_provider_detail_omits_identifiers_before_an_optional_path_segment() -> None:
    """An omitted optional suffix must not shift a required identifier out of redaction."""

    school_code = "994"

    def handler(request: httpx.Request) -> httpx.Response:
        """Echo the school code from a route whose optional student id was omitted."""

        return httpx.Response(
            400,
            request=request,
            json={"Message": f"School {school_code} was not found"},
        )

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.students.get_contacts(school_code=school_code)

    rendered = f"{raised.value!s} {raised.value.context!r}"
    assert school_code not in rendered
    assert raised.value.context is not None
    assert raised.value.context.path == (
        "/api/v5/schools/{SchoolCode}/contacts/{StudentID}"
    )
    assert raised.value.context.detail is None


def test_transport_error_does_not_retain_original_exception_chain() -> None:
    """A wrapped transport failure should not retain its credential-bearing request."""

    def handler(request: httpx.Request) -> httpx.Response:
        """Raise an httpx error carrying the complete live request."""

        raise httpx.ConnectError("network down", request=request)

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret-certificate",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesTransportError) as raised:
        client.request("GET", "/students", params={"token": "query-secret"})

    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_malformed_json_error_does_not_retain_response_document() -> None:
    """Malformed JSON should not remain reachable through a parser exception chain."""

    sensitive_body = b'{"RawBinary":"sensitive-picture-data"'

    def handler(request: httpx.Request) -> httpx.Response:
        """Return a bounded but malformed body containing sensitive data."""

        return httpx.Response(200, request=request, content=sensitive_body)

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.request("GET", "/students")

    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


def test_model_validation_error_does_not_retain_response_document() -> None:
    """Generated-model failures should expose a safe SDK error with scrubbed locals."""

    sensitive_body = b'[{"CellPhone":{"RawBinary":"sensitive-picture-data"}}]'

    def handler(request: httpx.Request) -> httpx.Response:
        """Return valid JSON whose documented scalar field has an invalid object value."""

        return httpx.Response(200, request=request, content=sensitive_body)

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.students.get_contacts(school_code=994)

    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None
    traceback = raised.value.__traceback__
    while traceback is not None and traceback.tb_frame.f_code.co_name != "validate_response":
        traceback = traceback.tb_next
    assert traceback is not None
    locals_ = traceback.tb_frame.f_locals
    assert locals_["response"] is None
    assert locals_["body"] is None
    assert locals_["payload"] is None
    assert locals_["state"] is None
    assert locals_["operation"] is None


def test_sync_send_traceback_clears_request_and_response_locals() -> None:
    """Sync SDK frames should not retain credentials, params, bodies, or the client."""

    def handler(request: httpx.Request) -> httpx.Response:
        """Return a provider error after receiving credential-bearing request data."""

        return httpx.Response(400, request=request, json={"Message": "Rejected"})

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="traceback-certificate",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError) as raised:
        client.request(
            "GET",
            "/students",
            params={"token": "traceback-query-secret"},
            json={"RawBinary": "traceback-picture-data"},
        )

    traceback = raised.value.__traceback__
    while traceback is not None and traceback.tb_frame.f_code.co_name != "_send":
        traceback = traceback.tb_next
    assert traceback is not None
    locals_ = traceback.tb_frame.f_locals
    assert locals_["self"] is None
    assert locals_["params"] is None
    assert locals_["json"] is None
    assert locals_["headers"] is None
    assert locals_["final_params"] == {}
    assert locals_["merged_headers"] == {}
    assert locals_["body"] == b""
    assert locals_["response"] is None


def test_retryable_response_is_closed_before_sync_backoff() -> None:
    """The sync client should release a retry response before sleeping."""

    responses: list[httpx.Response] = []
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        """Record the first response so its state can be checked during backoff."""

        nonlocal attempts
        attempts += 1
        status_code = 503 if attempts == 1 else 200
        body = (
            b'{"Message":"Try again"}'
            if status_code == 503
            else b'{"AeriesVersion":"1.0"}'
        )
        response = httpx.Response(
            status_code,
            request=request,
            stream=httpx.ByteStream(body),
        )
        responses.append(response)
        return response

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client:

        def assert_closed(_: int) -> None:
            """Replace the real delay and assert the stream has already exited."""

            assert responses[0].is_closed

        client._state.sleep = assert_closed
        result = client.system.get_aeries_installation_information()

    assert result.aeries_version == "1.0"


class RecordingSyncResponse:
    """Minimal response double that records the requested sync chunk size."""

    def __init__(self) -> None:
        """Create the request metadata needed by the size error helper."""

        self.request = httpx.Request("GET", "https://district.example.edu/api/v5/students")
        self.status_code = 200
        self.headers = httpx.Headers()
        self.is_stream_consumed = False
        self.chunk_size: int | None = None

    def iter_raw(self, chunk_size: int | None = None):  # type: ignore[no-untyped-def]
        """Yield an oversized chunk after recording the caller's requested bound."""

        self.chunk_size = chunk_size
        yield b"sensitive-picture-data"


def test_sync_reader_requests_bounded_chunks_and_drops_live_chunk() -> None:
    """The sync reader should request limit-sized chunks and clear traceback bytes."""

    response = RecordingSyncResponse()
    with pytest.raises(AeriesResponseTooLargeError) as raised:
        read_limited_response(  # type: ignore[arg-type]
            response,
            path="/students",
            max_response_bytes=5,
        )

    assert response.chunk_size == 6
    traceback = raised.value.__traceback__
    while traceback is not None and traceback.tb_frame.f_code.co_name != "read_limited_response":
        traceback = traceback.tb_next
    assert traceback is not None
    assert traceback.tb_frame.f_locals["chunk"] == b""
    assert traceback.tb_frame.f_locals["body"] == bytearray()


class FailingSyncResponse(RecordingSyncResponse):
    """Response double that fails after yielding sensitive partial bytes."""

    def iter_raw(self, chunk_size: int | None = None):  # type: ignore[no-untyped-def]
        """Yield one chunk and then simulate a custom transport stream failure."""

        self.chunk_size = chunk_size
        yield b"sensitive-picture-data"
        raise RuntimeError("custom stream failed")


def test_sync_reader_scrubs_partial_body_after_custom_stream_failure() -> None:
    """Unexpected sync stream errors must not retain already-read response bytes."""

    with pytest.raises(RuntimeError) as raised:
        read_limited_response(  # type: ignore[arg-type]
            FailingSyncResponse(),
            path="/students",
            max_response_bytes=100,
        )

    traceback = raised.value.__traceback__
    while traceback is not None and traceback.tb_frame.f_code.co_name != "read_limited_response":
        traceback = traceback.tb_next
    assert traceback is not None
    assert traceback.tb_frame.f_locals["chunk"] == b""
    assert traceback.tb_frame.f_locals["body"] == bytearray()
    assert traceback.tb_frame.f_locals["raw_iterator"] is None


class NeverReadSyncStream(httpx.SyncByteStream):
    """Response stream that fails if compressed bytes are ever consumed."""

    def __init__(self) -> None:
        """Track whether the client attempted to iterate compressed bytes."""

        self.was_read = False

    def __iter__(self):  # type: ignore[no-untyped-def]
        """Fail because encoded response bodies must be rejected before reading."""

        self.was_read = True
        raise AssertionError("compressed response body was read")


def test_sync_client_forces_identity_and_rejects_encoded_body_before_read() -> None:
    """The sync client should prevent HTTPX from expanding compressed responses."""

    stream = NeverReadSyncStream()

    def handler(request: httpx.Request) -> httpx.Response:
        """Return an encoded response even though the SDK requested identity."""

        assert request.headers["Accept-Encoding"] == "identity"
        return httpx.Response(
            200,
            request=request,
            headers={"Content-Encoding": "gzip"},
            stream=stream,
        )

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesValidationError):
        client.system.get_aeries_installation_information(
            headers={"Accept-Encoding": "gzip"}
        )

    assert not stream.was_read


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


@pytest.mark.asyncio
async def test_async_oversized_retryable_error_is_not_retried() -> None:
    """The async client should fail before retrying an oversized retryable error."""

    body = json.dumps({"Message": "retry later " * 40}).encode()
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        """Return one oversized 503 and expose any accidental second request."""

        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(503, request=request, content=body)
        return httpx.Response(200, request=request, json={"AeriesVersion": "1.0"})

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(body) - 1,
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(AeriesResponseTooLargeError):
            await client.system.get_aeries_installation_information()

    assert attempts == 1


@pytest.mark.asyncio
async def test_async_transport_error_does_not_retain_original_exception_chain() -> None:
    """The async wrapper should also detach the original credential-bearing request."""

    def handler(request: httpx.Request) -> httpx.Response:
        """Raise an httpx failure that keeps a reference to the request."""

        raise httpx.ConnectError("network down", request=request)

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret-certificate",
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(AeriesTransportError) as raised:
            await client.request("GET", "/students", params={"token": "query-secret"})

    assert raised.value.__cause__ is None
    assert raised.value.__context__ is None


@pytest.mark.asyncio
async def test_async_send_traceback_clears_request_and_response_locals() -> None:
    """Async SDK frames should clear request and response data before propagation."""

    def handler(request: httpx.Request) -> httpx.Response:
        """Return a provider error after receiving sensitive async request data."""

        return httpx.Response(400, request=request, json={"Message": "Rejected"})

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="traceback-certificate",
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(AeriesValidationError) as raised:
            await client.request(
                "GET",
                "/students",
                params={"token": "traceback-query-secret"},
                json={"RawBinary": "traceback-picture-data"},
            )

    traceback = raised.value.__traceback__
    while traceback is not None and traceback.tb_frame.f_code.co_name != "_send":
        traceback = traceback.tb_next
    assert traceback is not None
    locals_ = traceback.tb_frame.f_locals
    assert locals_["self"] is None
    assert locals_["params"] is None
    assert locals_["json"] is None
    assert locals_["headers"] is None
    assert locals_["final_params"] == {}
    assert locals_["merged_headers"] == {}
    assert locals_["body"] == b""
    assert locals_["response"] is None


@pytest.mark.asyncio
async def test_retryable_response_is_closed_before_async_backoff(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    """The async client should release a retry response before sleeping."""

    responses: list[httpx.Response] = []
    attempts = 0

    def handler(request: httpx.Request) -> httpx.Response:
        """Record responses so the patched delay can inspect the first stream."""

        nonlocal attempts
        attempts += 1
        status_code = 503 if attempts == 1 else 200
        body = (
            b'{"Message":"Try again"}'
            if status_code == 503
            else b'{"AeriesVersion":"1.0"}'
        )
        response = httpx.Response(
            status_code,
            request=request,
            stream=httpx.ByteStream(body),
        )
        responses.append(response)
        return response

    async def assert_closed(_: float) -> None:
        """Replace the real delay and assert the stream has already exited."""

        assert responses[0].is_closed

    monkeypatch.setattr("aeries_sis_sdk.async_client.asyncio.sleep", assert_closed)
    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client:
        result = await client.system.get_aeries_installation_information()

    assert result.aeries_version == "1.0"


class RecordingAsyncResponse:
    """Minimal response double that records the requested async chunk size."""

    def __init__(self) -> None:
        """Create the request metadata needed by the size error helper."""

        self.request = httpx.Request("GET", "https://district.example.edu/api/v5/students")
        self.status_code = 200
        self.headers = httpx.Headers()
        self.is_stream_consumed = False
        self.chunk_size: int | None = None

    async def aiter_raw(self, chunk_size: int | None = None):  # type: ignore[no-untyped-def]
        """Yield an oversized async chunk after recording the requested bound."""

        self.chunk_size = chunk_size
        yield b"sensitive-picture-data"


@pytest.mark.asyncio
async def test_async_reader_requests_bounded_chunks_and_drops_live_chunk() -> None:
    """The async reader should request limit-sized chunks and clear traceback bytes."""

    response = RecordingAsyncResponse()
    with pytest.raises(AeriesResponseTooLargeError) as raised:
        await read_limited_response_async(  # type: ignore[arg-type]
            response,
            path="/students",
            max_response_bytes=5,
        )

    assert response.chunk_size == 6
    traceback = raised.value.__traceback__
    while (
        traceback is not None
        and traceback.tb_frame.f_code.co_name != "read_limited_response_async"
    ):
        traceback = traceback.tb_next
    assert traceback is not None
    assert traceback.tb_frame.f_locals["chunk"] == b""
    assert traceback.tb_frame.f_locals["body"] == bytearray()


class FailingAsyncResponse(RecordingAsyncResponse):
    """Async response double that fails after yielding sensitive partial bytes."""

    async def aiter_raw(self, chunk_size: int | None = None):  # type: ignore[no-untyped-def]
        """Yield one chunk and then simulate an async custom stream failure."""

        self.chunk_size = chunk_size
        yield b"sensitive-picture-data"
        raise RuntimeError("custom async stream failed")


@pytest.mark.asyncio
async def test_async_reader_scrubs_partial_body_after_custom_stream_failure() -> None:
    """Unexpected async stream errors must not retain already-read response bytes."""

    with pytest.raises(RuntimeError) as raised:
        await read_limited_response_async(  # type: ignore[arg-type]
            FailingAsyncResponse(),
            path="/students",
            max_response_bytes=100,
        )

    traceback = raised.value.__traceback__
    while (
        traceback is not None
        and traceback.tb_frame.f_code.co_name != "read_limited_response_async"
    ):
        traceback = traceback.tb_next
    assert traceback is not None
    assert traceback.tb_frame.f_locals["chunk"] == b""
    assert traceback.tb_frame.f_locals["body"] == bytearray()
    assert traceback.tb_frame.f_locals["raw_iterator"] is None


class NeverReadAsyncStream(httpx.AsyncByteStream):
    """Async response stream that fails if compressed bytes are consumed."""

    def __init__(self) -> None:
        """Track whether async iteration was attempted."""

        self.was_read = False

    async def __aiter__(self):  # type: ignore[no-untyped-def]
        """Fail because encoded responses must be rejected before async reading."""

        self.was_read = True
        raise AssertionError("compressed response body was read")
        yield b""  # pragma: no cover


@pytest.mark.asyncio
async def test_async_client_forces_identity_and_rejects_encoded_body_before_read() -> None:
    """The async client should prevent HTTPX from expanding compressed responses."""

    stream = NeverReadAsyncStream()

    def handler(request: httpx.Request) -> httpx.Response:
        """Return an encoded response even though the SDK requested identity."""

        assert request.headers["Accept-Encoding"] == "identity"
        return httpx.Response(
            200,
            request=request,
            headers={"Content-Encoding": "gzip"},
            stream=stream,
        )

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(AeriesValidationError):
            await client.system.get_aeries_installation_information()

    assert not stream.was_read


def assert_size_traceback_has_no_live_httpx_response(error: BaseException) -> None:
    """Assert runtime size-error frames retain neither responses nor requests."""

    traceback = error.__traceback__
    runtime_frames = 0
    while traceback is not None:
        if traceback.tb_frame.f_globals.get("__name__") == "aeries_sis_sdk._runtime":
            runtime_frames += 1
            for value in traceback.tb_frame.f_locals.values():
                assert not isinstance(value, (httpx.Request, httpx.Response))
        traceback = traceback.tb_next
    assert runtime_frames


def test_size_error_traceback_has_no_live_httpx_response() -> None:
    """Size errors should be built from scalars after dropping the response object."""

    body = student_picture_body("cGhvdG8=" * 20)

    def handler(request: httpx.Request) -> httpx.Response:
        """Return an oversized student-picture body."""

        return httpx.Response(200, request=request, content=body)

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        max_response_bytes=len(body) - 1,
        transport=httpx.MockTransport(handler),
    ) as client, pytest.raises(AeriesResponseTooLargeError) as raised:
        client.students.get_student_picture(school_code=994, student_id=99400001)

    assert_size_traceback_has_no_live_httpx_response(raised.value)
