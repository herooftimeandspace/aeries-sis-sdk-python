"""Async runtime tests for the public async client."""

from __future__ import annotations

import httpx
import pytest

from aeries_sis_sdk import AsyncClient
from aeries_sis_sdk.errors import AeriesHTTPError


@pytest.mark.asyncio
async def test_async_client_calls_generated_system_namespace() -> None:
    """The async client should expose the generated namespaces and parse JSON."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            request=request,
            json={"AeriesVersion": "1.0", "DatabaseYear": "2024-2025"},
        )

    client = AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    )

    result = await client.system.get_aeries_installation_information()
    await client.aclose()

    assert result.database_year == "2024-2025"


@pytest.mark.asyncio
async def test_async_client_retries_safe_get_requests() -> None:
    """The async client should retry safe GET requests after a transient error."""

    attempts = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        attempts["count"] += 1
        if attempts["count"] == 1:
            return httpx.Response(503, request=request, json={"Message": "Try again"})
        return httpx.Response(
            200,
            request=request,
            json={"AeriesVersion": "1.0", "DatabaseYear": "2024-2025"},
        )

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client:
        result = await client.system.get_aeries_installation_information()

    assert attempts["count"] == 2
    assert result.aeries_version == "1.0"


@pytest.mark.asyncio
async def test_async_client_does_not_retry_side_effect_get_requests() -> None:
    """The async client should not retry pre-enrollment trigger endpoints."""

    attempts = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        attempts["count"] += 1
        return httpx.Response(503, request=request, json={"Message": "Try again"})

    async with AsyncClient(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client:
        with pytest.raises(AeriesHTTPError):
            await client.pre_enrollment.pre_enroll_student(student_id=99400001)

    assert attempts["count"] == 1
