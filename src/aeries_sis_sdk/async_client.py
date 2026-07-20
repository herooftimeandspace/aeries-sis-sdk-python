"""Public async client for the Aeries SIS SDK."""

from __future__ import annotations

import asyncio
from collections.abc import Mapping
from typing import Any

import httpx

from ._runtime import (
    DEFAULT_MAX_RESPONSE_BYTES,
    RuntimeState,
    read_limited_response_async,
    safe_request_path,
    validate_response,
    wrap_transport_error,
)
from .generated import ASYNC_NAMESPACE_REGISTRY


class AsyncClient:
    """Asynchronous Aeries API client.

    This client mirrors the sync API closely so callers can switch between sync
    and async styles without learning a new surface area.
    """

    def __init__(
        self,
        *,
        base_url: str,
        certificate: str,
        default_database_year: str | int | None = None,
        timeout: float = 30.0,
        user_agent: str = "aeries-sis-sdk-python/0.1.0",
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
        transport: httpx.AsyncBaseTransport | None = None,
        session: httpx.AsyncClient | None = None,
    ) -> None:
        """Create an async client and attach all generated namespaces.

        ``max_response_bytes`` has the same positive-integer validation and
        decoded-body semantics as the synchronous client so applications can
        switch execution styles without changing their safety policy.
        """

        self._state = RuntimeState(
            base_url=base_url,
            certificate=certificate,
            default_database_year=default_database_year,
            timeout=timeout,
            user_agent=user_agent,
            max_response_bytes=max_response_bytes,
        )
        self._owns_session = session is None
        self._session = session or httpx.AsyncClient(
            base_url=self._state.base_url,
            timeout=self._state.timeout,
            transport=transport,
        )
        for namespace_name, namespace_type in ASYNC_NAMESPACE_REGISTRY.items():
            setattr(self, namespace_name, namespace_type(self))

    async def aclose(self) -> None:
        """Close the underlying async HTTP session when this client owns it."""

        if self._owns_session:
            await self._session.aclose()

    async def __aenter__(self) -> AsyncClient:
        """Support use in an async context manager block."""

        return self

    async def __aexit__(self, *_: object) -> None:
        """Close the HTTP session at the end of a context manager block."""

        await self.aclose()

    async def request(
        self,
        method: str,
        path: str,
        *,
        path_params: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        json: Any = None,
        headers: Mapping[str, str] | None = None,
        database_year: str | int | None = None,
        timeout: float | None = None,
    ) -> Any:
        """Send one raw JSON request to the Aeries API."""

        operation = self._state.operation_for_request(method=method, path=path)
        return await self._send(
            method=method,
            path=path,
            operation=operation,
            path_params=path_params,
            params=params,
            json=json,
            headers=headers,
            database_year=database_year,
            timeout=timeout,
        )

    async def _call_operation(
        self,
        operation_id: str,
        *,
        path_params: dict[str, Any] | None = None,
        params: dict[str, Any] | None = None,
        json: Any = None,
        headers: Mapping[str, str] | None = None,
        database_year: str | int | None = None,
        timeout: float | None = None,
    ) -> Any:
        """Execute one generated operation by looking it up in the contract."""

        operation = self._state.operation_for_request(
            method="GET",
            path="",
            operation_id=operation_id,
        )
        if operation is None:
            raise LookupError(f"Unknown generated operation: {operation_id}")
        return await self._send(
            method=operation.method,
            path=operation.path_template,
            operation=operation,
            path_params=path_params,
            params=params,
            json=json,
            headers=headers,
            database_year=database_year,
            timeout=timeout,
        )

    async def _send(
        self,
        *,
        method: str,
        path: str,
        operation: Any,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        json: Any,
        headers: Mapping[str, str] | None,
        database_year: str | int | None,
        timeout: float | None,
    ) -> Any:
        """Send a request with contract-aware retry behavior."""

        request_method, final_path, final_params = self._state.request_parts(
            method=method,
            path=path,
            path_params=path_params,
            params=params,
            database_year=database_year,
            operation=operation,
        )
        merged_headers = self._state.headers(headers)
        context_path = safe_request_path(operation, final_path)
        max_attempts = 3 if self._state.should_retry(operation) else 1
        for attempt in range(1, max_attempts + 1):
            try:
                async with self._session.stream(
                    request_method,
                    final_path,
                    params=final_params,
                    json=json,
                    headers=merged_headers,
                    timeout=timeout or self._state.timeout,
                ) as response:
                    if attempt < max_attempts and self._state.should_retry(
                        operation, response.status_code
                    ):
                        await asyncio.sleep(0.2 * attempt)
                        continue
                    body = await read_limited_response_async(
                        response,
                        path=context_path,
                        max_response_bytes=self._state.max_response_bytes,
                    )
                    return validate_response(
                        state=self._state,
                        operation=operation,
                        response=response,
                        body=body,
                        path=context_path,
                    )
            except httpx.HTTPError as exc:
                if attempt < max_attempts and self._state.should_retry(operation):
                    await asyncio.sleep(0.2 * attempt)
                    continue
                raise wrap_transport_error(request_method, context_path, exc) from exc
        raise RuntimeError("Unreachable retry loop exit in async client.")
