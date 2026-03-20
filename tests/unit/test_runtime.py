"""Unit tests for the hand-written runtime helpers."""

from __future__ import annotations

import httpx
import pytest

from aeries_sis_sdk._runtime import build_client_base_url, parse_error_response
from aeries_sis_sdk.auth import build_headers, redact_secret
from aeries_sis_sdk.client import Client
from aeries_sis_sdk.contracts import (
    find_operation_by_id,
    format_path,
    load_contract,
    merge_query_params,
)
from aeries_sis_sdk.errors import (
    AeriesHTTPError,
    AeriesNotFoundError,
    AeriesTransportError,
    AeriesValidationError,
)
from aeries_sis_sdk.models import AeriesModel, parse_payload


def test_build_client_base_url_normalizes_api_root() -> None:
    """The runtime should always talk to `/api/v5` regardless of input form."""

    assert build_client_base_url("https://district.example.edu/aeries") == (
        "https://district.example.edu/aeries/api/v5"
    )
    assert build_client_base_url("https://district.example.edu/aeries/api/v5") == (
        "https://district.example.edu/aeries/api/v5"
    )


def test_redact_secret_hides_middle_characters() -> None:
    """Error messages should show only a safe hint of the certificate."""

    assert redact_secret("abcdef") == "ab**ef"
    assert redact_secret("abc") == "***"


def test_build_headers_merges_extra_headers() -> None:
    """Callers can add safe headers without losing required auth headers."""

    headers = build_headers(
        certificate="secret",
        user_agent="sdk-test",
        extra_headers={"X-Trace-ID": "trace"},
    )
    assert headers["AERIES-CERT"] == "secret"
    assert headers["Accept"] == "application/json"
    assert headers["X-Trace-ID"] == "trace"


def test_merge_query_params_includes_database_year() -> None:
    """DatabaseYear should be added when callers or defaults provide it."""

    params = merge_query_params(
        params={"SchoolCode": 994},
        database_year=None,
        default_database_year=2024,
    )
    assert params["DatabaseYear"] == "2024"
    assert params["SchoolCode"] == 994


def test_parse_error_response_uses_message_payload() -> None:
    """The SDK should surface the human-readable `Message` body when present."""

    request = httpx.Request("GET", "https://district.example.edu/aeries/api/v5/staff/1")
    response = httpx.Response(404, request=request, json={"Message": "Invalid Staff ID"})
    error = parse_error_response(response)
    assert isinstance(error, AeriesNotFoundError)
    assert "Invalid Staff ID" in str(error)


def test_client_retries_safe_get_requests() -> None:
    """A safe GET should retry once after a transient server error."""

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

    client = Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    )

    result = client.system.get_aeries_installation_information()
    client.close()

    assert attempts["count"] == 2
    assert result.aeries_version == "1.0"


def test_client_does_not_retry_side_effect_get_requests() -> None:
    """Command-style GET endpoints must not be retried automatically."""

    attempts = {"count": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        attempts["count"] += 1
        return httpx.Response(503, request=request, json={"Message": "Try again"})

    client = Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    )

    with pytest.raises(AeriesHTTPError):
        client.pre_enrollment.pre_enroll_student(student_id=99400001)
    client.close()

    assert attempts["count"] == 1


def test_sync_client_context_manager_closes_cleanly() -> None:
    """The sync client should support `with Client(...)` blocks."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, request=request, json={"AeriesVersion": "1.0"})

    with Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    ) as client:
        result = client.system.get_aeries_installation_information()

    assert result.aeries_version == "1.0"


def test_request_merges_headers_and_database_year() -> None:
    """The low-level request API should send the plan-required headers."""

    seen: dict[str, str] = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["path"] = request.url.path
        seen["query"] = str(request.url.query.decode())
        seen["accept"] = request.headers["Accept"]
        seen["certificate"] = request.headers["AERIES-CERT"]
        return httpx.Response(
            200,
            request=request,
            json=[{"SchoolCode": 994, "SchoolName": "Aeries High"}],
        )

    client = Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        default_database_year=2024,
        transport=httpx.MockTransport(handler),
    )

    result = client.schools.get_school_information(school_code=994)
    client.close()

    assert seen["path"].endswith("/api/v5/schools/994")
    assert "DatabaseYear=2024" in seen["query"]
    assert seen["accept"] == "application/json"
    assert seen["certificate"] == "secret"
    assert result[0].school_code in {994, "994"}


def test_format_path_drops_missing_optional_segments() -> None:
    """Optional placeholders should disappear instead of rendering `None`."""

    path = format_path(
        "/api/v5/schools/{SchoolCode}",
        path_params={"SchoolCode": None},
        optional_path_parameter_names={"SchoolCode"},
    )
    assert path == "/api/v5/schools"


def test_find_operation_by_id_raises_for_unknown_operation() -> None:
    """The contract lookup helper should fail loudly on bad ids."""

    contract = load_contract()
    with pytest.raises(LookupError):
        find_operation_by_id(contract, "missing.operation")


def test_transport_errors_are_wrapped() -> None:
    """Network failures should surface as AeriesTransportError."""

    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("network down", request=request)

    client = Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    )

    with pytest.raises(AeriesTransportError):
        client.system.get_aeries_installation_information()
    client.close()


def test_invalid_json_response_raises_validation_error() -> None:
    """Non-JSON success bodies should raise a validation error."""

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, request=request, text="not-json")

    client = Client(
        base_url="https://district.example.edu/aeries",
        certificate="secret",
        transport=httpx.MockTransport(handler),
    )

    with pytest.raises(AeriesValidationError):
        client.system.get_aeries_installation_information()
    client.close()


def test_packaged_contract_contains_expected_categories() -> None:
    """The packaged contract snapshot should expose all planned namespaces."""

    contract = load_contract()
    categories = {operation.category for operation in contract.operations}
    assert {"system", "schools", "students", "gradebook", "pre_enrollment"} <= categories


class ExampleModel(AeriesModel):
    """Small helper model used to cover scalar parse behavior."""

    name: str | None = None


def test_parse_payload_returns_scalars_unchanged() -> None:
    """Scalar payloads should pass through without Pydantic validation."""

    assert parse_payload(ExampleModel, "raw-value") == "raw-value"
