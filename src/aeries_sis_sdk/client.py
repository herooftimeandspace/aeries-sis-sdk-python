"""Public sync client for the Aeries SIS SDK."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx

from ._runtime import RuntimeState, validate_response, wrap_transport_error
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
        transport: httpx.BaseTransport | None = None,
        session: httpx.Client | None = None,
    ) -> None:
        """Create a sync client and attach all generated namespaces."""

        self._state = RuntimeState(
            base_url=base_url,
            certificate=certificate,
            default_database_year=default_database_year,
            timeout=timeout,
            user_agent=user_agent,
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

        request_method, final_path, final_params = self._state.request_parts(
            method=method,
            path=path,
            path_params=path_params,
            params=params,
            database_year=database_year,
            operation=operation,
        )
        merged_headers = self._state.headers(headers)
        max_attempts = 3 if self._state.should_retry(operation) else 1
        for attempt in range(1, max_attempts + 1):
            try:
                response = self._session.request(
                    request_method,
                    final_path,
                    params=final_params,
                    json=json,
                    headers=merged_headers,
                    timeout=timeout or self._state.timeout,
                )
            except httpx.HTTPError as exc:
                if attempt < max_attempts and self._state.should_retry(operation):
                    self._state.sleep(attempt)
                    continue
                raise wrap_transport_error(request_method, final_path, exc) from exc
            if response.status_code < 400:
                return validate_response(state=self._state, operation=operation, response=response)
            if attempt < max_attempts and self._state.should_retry(operation, response.status_code):
                self._state.sleep(attempt)
                continue
            return validate_response(state=self._state, operation=operation, response=response)
        raise RuntimeError("Unreachable retry loop exit in sync client.")
