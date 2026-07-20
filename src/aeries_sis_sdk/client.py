"""Public sync client for the Aeries SIS SDK."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx

from ._runtime import (
    DEFAULT_MAX_RESPONSE_BYTES,
    RuntimeState,
    read_limited_response,
    safe_request_path,
    validate_response,
    wrap_transport_error,
)
from .generated import NAMESPACE_REGISTRY


class Client:
    """Synchronous Aeries API client.

    This class is the main entry point for normal Python scripts and services.
    It exposes a low-level `request` method plus generated namespaces such as
    `client.schools` and `client.students`.
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
        transport: httpx.BaseTransport | None = None,
        session: httpx.Client | None = None,
    ) -> None:
        """Create a sync client and attach all generated namespaces.

        ``max_response_bytes`` must be a positive integer. It limits decoded
        response bytes for every status code and prevents large student-picture
        or provider-error payloads from being buffered without an SDK-owned cap.
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
        self._session = session or httpx.Client(
            base_url=self._state.base_url,
            timeout=self._state.timeout,
            transport=transport,
        )
        for namespace_name, namespace_type in NAMESPACE_REGISTRY.items():
            setattr(self, namespace_name, namespace_type(self))

    def close(self) -> None:
        """Close the underlying HTTP session when this client owns it."""

        if self._owns_session:
            self._session.close()

    def __enter__(self) -> Client:
        """Support use in a context manager block."""

        return self

    def __exit__(self, *_: object) -> None:
        """Close the HTTP session at the end of a context manager block."""

        self.close()

    def request(
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
        """Send one raw JSON request to the Aeries API.

        This method is intentionally thin. The generated namespaces call into it,
        but advanced users can also call it directly for low-level access.
        """

        operation = self._state.operation_for_request(method=method, path=path)
        return self._send(
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

    def _call_operation(
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
        return self._send(
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

    def _send(
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
        """Send a request with retry behavior driven by the contract metadata."""

        request_method = ""
        final_path = ""
        final_params: dict[str, Any] = {}
        merged_headers: dict[str, str] = {}
        context_path = ""
        body = b""
        response: httpx.Response | None = None
        current_response: httpx.Response | None = None
        transport_error = None
        try:
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
                retry_transport = False
                transport_error = None
                try:
                    with self._session.stream(
                        request_method,
                        final_path,
                        params=final_params,
                        json=json,
                        headers=merged_headers,
                        timeout=timeout or self._state.timeout,
                    ) as current_response:
                        response = current_response
                        # Read every status through the bound before deciding to
                        # retry, then leave the context so backoff holds no socket.
                        body = read_limited_response(
                            current_response,
                            path=context_path,
                            max_response_bytes=self._state.max_response_bytes,
                        )
                except httpx.HTTPError as exc:
                    if attempt < max_attempts and self._state.should_retry(operation):
                        retry_transport = True
                    else:
                        transport_error = wrap_transport_error(
                            request_method,
                            context_path,
                            exc,
                        )
                if transport_error is not None:
                    # Raise outside the active httpx handler; the outer finally
                    # clears every request-bearing local before propagation.
                    raise transport_error
                if retry_transport:
                    self._state.sleep(attempt)
                    continue
                if response is None:
                    raise RuntimeError("A response was not available after a successful send.")
                if attempt < max_attempts and self._state.should_retry(
                    operation, response.status_code
                ):
                    self._state.sleep(attempt)
                    continue
                return validate_response(
                    state=self._state,
                    operation=operation,
                    response=response,
                    body=body,
                    path=context_path,
                )
            raise RuntimeError("Unreachable retry loop exit in sync client.")
        finally:
            # Traceback collectors can retain frame locals. Drop all caller,
            # request, response, body, session, and credential references before
            # any exception leaves this SDK transport frame.
            method = ""
            path = ""
            operation = None
            path_params = None
            params = None
            json = None
            headers = None
            database_year = None
            timeout = None
            request_method = ""
            final_path = ""
            final_params.clear()
            merged_headers.clear()
            context_path = ""
            body = b""
            response = None
            current_response = None
            transport_error = None
            self = None  # type: ignore[assignment]
