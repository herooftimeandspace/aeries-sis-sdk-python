"""Shared runtime helpers for sync and async Aeries clients."""

from __future__ import annotations

import time
from collections.abc import Mapping
from typing import Any

import httpx

from .auth import build_headers
from .contract_types import ContractOperation
from .contracts import (
    find_operation_by_id,
    format_path,
    load_contract,
    maybe_match_operation,
    merge_query_params,
)
from .errors import (
    AeriesAuthError,
    AeriesHTTPError,
    AeriesNotFoundError,
    AeriesTransportError,
    AeriesValidationError,
    ErrorContext,
)
from .generated.models import MODEL_REGISTRY
from .models import parse_payload

RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}


def build_client_base_url(base_url: str) -> str:
    """Normalize a tenant URL so the runtime always talks to `/api/v5`."""

    normalized = base_url.rstrip("/")
    if normalized.endswith("/api/v5"):
        return normalized
    if normalized.endswith("/api"):
        return f"{normalized}/v5"
    return f"{normalized}/api/v5"


def parse_error_response(response: httpx.Response) -> Exception:
    """Turn an HTTP response into the most specific SDK exception we can."""

    detail: str | None = None
    try:
        payload = response.json()
    except ValueError:
        payload = None
    if isinstance(payload, dict):
        detail_value = payload.get("Message")
        if isinstance(detail_value, str):
            detail = detail_value
    context = ErrorContext(
        method=response.request.method,
        url=str(response.request.url),
        status_code=response.status_code,
        detail=detail,
    )
    message = detail or f"Aeries API returned HTTP {response.status_code}"
    if response.status_code in {401, 403}:
        return AeriesAuthError(message, context=context)
    if response.status_code == 404:
        return AeriesNotFoundError(message, context=context)
    if response.status_code in {400, 422}:
        return AeriesValidationError(message, context=context)
    return AeriesHTTPError(message, context=context)


class RuntimeState:
    """Carry state shared by sync and async clients.

    The runtime state keeps contract data and request configuration together so
    the sync and async clients can share the same validation and retry rules.
    """

    def __init__(
        self,
        *,
        base_url: str,
        certificate: str,
        default_database_year: str | int | None,
        timeout: float,
        user_agent: str,
    ) -> None:
        """Store connection settings and the packaged contract snapshot."""

        self.base_url = build_client_base_url(base_url)
        self.certificate = certificate
        self.default_database_year = default_database_year
        self.timeout = timeout
        self.user_agent = user_agent
        self.contract = load_contract()

    def operation_for_request(
        self, *, method: str, path: str, operation_id: str | None = None
    ) -> ContractOperation | None:
        """Resolve an operation by id first, then by exact method/template pair."""

        if operation_id:
            return find_operation_by_id(self.contract, operation_id)
        return maybe_match_operation(self.contract, method, path)

    def headers(self, extra_headers: Mapping[str, str] | None = None) -> dict[str, str]:
        """Build request headers with the project-standard JSON defaults."""

        return build_headers(
            certificate=self.certificate,
            user_agent=self.user_agent,
            extra_headers=extra_headers,
        )

    def request_parts(
        self,
        *,
        method: str,
        path: str,
        path_params: dict[str, Any] | None,
        params: dict[str, Any] | None,
        database_year: str | int | None,
        operation: ContractOperation | None,
    ) -> tuple[str, str, dict[str, Any]]:
        """Return the normalized method, final path, and merged query params."""

        optional_names = {
            parameter.name
            for parameter in (operation.path_parameters if operation else [])
            if not parameter.required
        }
        final_path = format_path(
            path,
            path_params=path_params,
            optional_path_parameter_names=optional_names,
        )
        final_params = merge_query_params(
            params=params,
            database_year=database_year,
            default_database_year=self.default_database_year,
        )
        return method.upper(), final_path, final_params

    def should_retry(
        self, operation: ContractOperation | None, status_code: int | None = None
    ) -> bool:
        """Decide whether a failed call is safe to retry automatically."""

        if operation is None or operation.side_effect:
            return False
        if status_code is None:
            return operation.method == "GET"
        return status_code in RETRYABLE_STATUS_CODES

    def parse_operation_payload(self, operation: ContractOperation | None, payload: Any) -> Any:
        """Return parsed Pydantic models for generated operations when possible."""

        if operation is None:
            return payload
        model_type = MODEL_REGISTRY.get(operation.response_model_name)
        if model_type is None:
            return payload
        return parse_payload(model_type, payload)

    def sleep(self, attempt: int) -> None:
        """Pause between retries with a tiny linear backoff."""

        time.sleep(0.2 * attempt)


def validate_response(
    *,
    state: RuntimeState,
    operation: ContractOperation | None,
    response: httpx.Response,
) -> Any:
    """Validate a response and return parsed JSON or raise an SDK exception."""

    if response.status_code >= 400:
        raise parse_error_response(response)
    if response.status_code == 204:
        return None
    try:
        payload = response.json()
    except ValueError as exc:
        context = ErrorContext(
            method=response.request.method,
            url=str(response.request.url),
            status_code=response.status_code,
            detail="Response body was not valid JSON.",
        )
        raise AeriesValidationError("Aeries API returned invalid JSON.", context=context) from exc
    return state.parse_operation_payload(operation, payload)


def wrap_transport_error(method: str, url: str, error: Exception) -> AeriesTransportError:
    """Convert an httpx transport error into the SDK transport exception type."""

    context = ErrorContext(method=method, url=url, detail=str(error))
    return AeriesTransportError("Unable to reach the Aeries API.", context=context)
