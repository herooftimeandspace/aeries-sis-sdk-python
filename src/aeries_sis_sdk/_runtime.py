"""Shared runtime helpers for sync and async Aeries clients."""

from __future__ import annotations

import json
import re
import time
from collections.abc import AsyncIterator, Iterator, Mapping
from typing import Any
from urllib.parse import unquote

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
    AeriesResponseTooLargeError,
    AeriesTransportError,
    AeriesValidationError,
    ErrorContext,
)
from .generated.models import MODEL_REGISTRY
from .models import parse_payload

RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
DEFAULT_MAX_RESPONSE_BYTES = 16 * 1024 * 1024
MAX_ERROR_DETAIL_CHARACTERS = 512
MAX_RESPONSE_CHUNK_BYTES = 64 * 1024
LONG_ENCODED_VALUE_PATTERN = re.compile(r"[A-Za-z0-9+/=_-]{128,}")


def build_client_base_url(base_url: str) -> str:
    """Normalize a tenant URL so the runtime always talks to `/api/v5`."""

    normalized = base_url.rstrip("/")
    if normalized.endswith("/api/v5"):
        return normalized
    if normalized.endswith("/api"):
        return f"{normalized}/v5"
    return f"{normalized}/api/v5"


def validate_max_response_bytes(value: int) -> int:
    """Return a valid response limit or reject unsafe constructor input.

    A boolean is rejected explicitly because Python treats booleans as integers,
    while a value such as ``True`` is not a meaningful byte budget for callers.
    """

    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("max_response_bytes must be a positive integer.")
    if value <= 0:
        raise ValueError("max_response_bytes must be a positive integer.")
    return value


def safe_request_path(
    operation: ContractOperation | None,
    fallback_path: str,
) -> str:
    """Choose a query-free contract path for exception context.

    Generated operations use the documented template so identifiers substituted
    into the live URL do not become part of routinely logged exception metadata.
    Low-level requests retain only the caller-provided path without its query.
    """

    if operation is not None:
        return operation.path_template
    return fallback_path.split("?", maxsplit=1)[0]


def sanitize_provider_detail(detail: str, *, secrets: tuple[str, ...] = ()) -> str | None:
    """Return bounded provider text only when it is safe diagnostic context.

    Control characters are folded into spaces. Messages containing a known
    credential, a URL, a query string, or a long encoded value are discarded in
    full because trying to redact unknown provider data could leave reusable or
    student-specific information behind.
    """

    normalized = " ".join(detail.split())
    if not normalized:
        return None
    if any(secret and secret in normalized for secret in secrets):
        return None
    lowered = normalized.casefold()
    if "://" in lowered or "?" in normalized or LONG_ENCODED_VALUE_PATTERN.search(normalized):
        return None
    return normalized[:MAX_ERROR_DETAIL_CHARACTERS]


def request_values_to_redact(
    request: httpx.Request,
    *,
    safe_path: str | None = None,
) -> tuple[str, ...]:
    """Collect actual request values that provider diagnostics must not echo.

    Query parameters and headers may contain per-call credentials that differ
    from constructor settings. Treat every non-empty value as sensitive rather
    than trying to infer which custom names a caller considers confidential.
    """

    # Use the fully built request because caller overrides may replace the
    # constructor certificate or add sensitive custom query/header values.
    values = [value for _, value in request.url.params.multi_items() if value]
    values.extend(value for value in request.headers.values() if value)
    if safe_path:
        template_segments = safe_path.strip("/").split("/")
        actual_segments = unquote(request.url.path).strip("/").split("/")
        # Base URLs may add leading tenant segments. Align the documented path
        # from the right before collecting values substituted for placeholders.
        if len(actual_segments) >= len(template_segments):
            actual_segments = actual_segments[-len(template_segments) :]
            values.extend(
                actual
                for template, actual in zip(template_segments, actual_segments, strict=True)
                if "{" in template and "}" in template and actual
            )
    return tuple(dict.fromkeys(values))


def parse_error_response(
    response: httpx.Response,
    *,
    body: bytes | None = None,
    path: str | None = None,
    certificate: str = "",
) -> Exception:
    """Turn a bounded HTTP response into the most specific safe SDK exception."""

    detail: str | None = None
    try:
        payload = json.loads(response.content if body is None else body)
    except (UnicodeDecodeError, ValueError):
        payload = None
    if isinstance(payload, dict):
        detail_value = payload.get("Message")
        if isinstance(detail_value, str):
            request_secrets = request_values_to_redact(response.request, safe_path=path)
            detail = sanitize_provider_detail(
                detail_value,
                secrets=(*request_secrets, certificate),
            )
    context = ErrorContext(
        method=response.request.method,
        path=path or response.request.url.path,
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
        max_response_bytes: int = DEFAULT_MAX_RESPONSE_BYTES,
    ) -> None:
        """Store connection settings and the packaged contract snapshot."""

        self.base_url = build_client_base_url(base_url)
        self.certificate = certificate
        self.default_database_year = default_database_year
        self.timeout = timeout
        self.user_agent = user_agent
        self.max_response_bytes = validate_max_response_bytes(max_response_bytes)
        self.contract = load_contract()

    def operation_for_request(
        self, *, method: str, path: str, operation_id: str | None = None
    ) -> ContractOperation | None:
        """Resolve an operation by id first, then by exact method/template pair."""

        if operation_id:
            return find_operation_by_id(self.contract, operation_id)
        return maybe_match_operation(self.contract, method, path)

    def headers(self, extra_headers: Mapping[str, str] | None = None) -> dict[str, str]:
        """Build JSON headers and require identity response encoding."""

        headers = build_headers(
            certificate=self.certificate,
            user_agent=self.user_agent,
            extra_headers=extra_headers,
        )
        # Counting raw identity bytes prevents httpx from expanding compressed
        # content before the SDK can enforce the response limit.
        headers["Accept-Encoding"] = "identity"
        return headers

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
    body: bytes | None = None,
    path: str | None = None,
) -> Any:
    """Validate a bounded response and return parsed JSON or raise an SDK exception."""

    if response.status_code >= 400:
        error = parse_error_response(
            response,
            body=body,
            path=path,
            certificate=state.certificate,
        )
        # Drop request, response, and body objects before this frame enters the
        # traceback retained by the sanitized SDK exception.
        response = None  # type: ignore[assignment]
        body = None
        state = None  # type: ignore[assignment]
        operation = None
        path = None
        raise error
    if response.status_code == 204:
        return None
    invalid_json = False
    try:
        payload = json.loads(response.content if body is None else body)
    except (UnicodeDecodeError, ValueError):
        invalid_json = True
    if invalid_json:
        context = ErrorContext(
            method=response.request.method,
            path=path or response.request.url.path,
            status_code=response.status_code,
            detail="Response body was not valid JSON.",
        )
        # Raise after leaving the parser exception handler so JSONDecodeError
        # cannot retain its full response document through exception chaining.
        error = AeriesValidationError("Aeries API returned invalid JSON.", context=context)
        response = None  # type: ignore[assignment]
        body = None
        state = None  # type: ignore[assignment]
        operation = None
        path = None
        raise error
    return state.parse_operation_payload(operation, payload)


def response_too_large_error(
    *,
    method: str,
    status_code: int,
    path: str,
    max_response_bytes: int,
) -> AeriesResponseTooLargeError:
    """Build a typed size failure entirely from safe scalar metadata."""

    context = ErrorContext(
        method=method,
        path=path,
        status_code=status_code,
        detail=f"Response exceeded the {max_response_bytes}-byte limit.",
    )
    return AeriesResponseTooLargeError(
        f"Aeries API response exceeded the {max_response_bytes}-byte limit.",
        context=context,
    )


def unsupported_content_encoding_error(
    *,
    method: str,
    status_code: int,
    path: str,
) -> AeriesValidationError:
    """Build a safe failure for a server that ignored identity encoding."""

    context = ErrorContext(
        method=method,
        path=path,
        status_code=status_code,
        detail="Compressed response bodies are not accepted.",
    )
    return AeriesValidationError(
        "Aeries API returned an unsupported compressed response.",
        context=context,
    )


def read_limited_response(
    response: httpx.Response,
    *,
    path: str,
    max_response_bytes: int,
) -> bytes:
    """Read at most the configured limit plus one decoded response byte.

    Reading one extra byte distinguishes an allowed body exactly at the limit
    from an oversized body. The temporary buffer is cleared before raising so
    the exception cannot accidentally retain photo or provider-error bytes.
    """

    method = response.request.method
    status_code = response.status_code
    content_encoding = response.headers.get("Content-Encoding", "identity").strip().casefold()
    if content_encoding not in {"", "identity"}:
        encoding_error = unsupported_content_encoding_error(
            method=method,
            status_code=status_code,
            path=path,
        )
        response = None  # type: ignore[assignment]
        raise encoding_error

    body = bytearray()
    chunk_size = min(MAX_RESPONSE_CHUNK_BYTES, max_response_bytes + 1)
    if response.is_stream_consumed:
        raw_iterator: Iterator[bytes] | None = iter((response.content,))
    else:
        # Identity encoding lets the SDK count transport bytes directly without
        # httpx materializing decoded data before the limit check.
        raw_iterator = response.iter_raw(chunk_size=chunk_size)
    response = None  # type: ignore[assignment]
    while raw_iterator is not None:
        try:
            chunk = next(raw_iterator)
        except StopIteration:
            raw_iterator = None
            break
        remaining = max_response_bytes + 1 - len(body)
        body.extend(chunk[:remaining])
        if len(body) > max_response_bytes:
            size_error = response_too_large_error(
                method=method,
                status_code=status_code,
                path=path,
                max_response_bytes=max_response_bytes,
            )
            body.clear()
            chunk = b""
            raw_iterator = None
            raise size_error
    return bytes(body)


async def read_limited_response_async(
    response: httpx.Response,
    *,
    path: str,
    max_response_bytes: int,
) -> bytes:
    """Asynchronously read a response with the same limit-plus-one policy."""

    method = response.request.method
    status_code = response.status_code
    content_encoding = response.headers.get("Content-Encoding", "identity").strip().casefold()
    if content_encoding not in {"", "identity"}:
        encoding_error = unsupported_content_encoding_error(
            method=method,
            status_code=status_code,
            path=path,
        )
        response = None  # type: ignore[assignment]
        raise encoding_error

    body = bytearray()
    chunk_size = min(MAX_RESPONSE_CHUNK_BYTES, max_response_bytes + 1)
    loaded_content = b""
    if response.is_stream_consumed:
        loaded_content = response.content

        async def loaded_iterator() -> AsyncIterator[bytes]:
            """Yield one already-loaded body for custom test transports."""

            yield loaded_content

        raw_iterator: AsyncIterator[bytes] | None = loaded_iterator()
    else:
        # Mirror the sync path by counting raw identity bytes before parsing.
        raw_iterator = response.aiter_raw(chunk_size=chunk_size)
    response = None  # type: ignore[assignment]
    while raw_iterator is not None:
        try:
            chunk = await anext(raw_iterator)
        except StopAsyncIteration:
            raw_iterator = None
            break
        remaining = max_response_bytes + 1 - len(body)
        body.extend(chunk[:remaining])
        if len(body) > max_response_bytes:
            size_error = response_too_large_error(
                method=method,
                status_code=status_code,
                path=path,
                max_response_bytes=max_response_bytes,
            )
            body.clear()
            chunk = b""
            loaded_content = b""
            raw_iterator = None
            raise size_error
    return bytes(body)


def wrap_transport_error(method: str, path: str, error: Exception) -> AeriesTransportError:
    """Convert an httpx transport error into a credential-safe SDK exception."""

    del error
    context = ErrorContext(method=method, path=path)
    return AeriesTransportError("Unable to reach the Aeries API.", context=context)
