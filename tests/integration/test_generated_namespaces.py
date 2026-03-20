"""Integration-style tests that cover the generated namespace surface."""

from __future__ import annotations

from inspect import getmembers, ismethod

import pytest
from tests.conftest import build_call_kwargs

from aeries_sis_sdk.generated import ASYNC_NAMESPACE_REGISTRY, NAMESPACE_REGISTRY
from aeries_sis_sdk.generated.models import MODEL_REGISTRY


class RecordingClient:
    """A tiny fake client that records generated sync namespace calls."""

    def __init__(self) -> None:
        """Initialize the call history for later assertions."""

        self.calls: list[tuple[str, dict[str, object]]] = []

    def _call_operation(self, operation_id: str, **kwargs: object) -> str:
        """Record the operation id and arguments instead of sending HTTP."""

        self.calls.append((operation_id, kwargs))
        return operation_id


class RecordingAsyncClient:
    """A tiny fake client that records generated async namespace calls."""

    def __init__(self) -> None:
        """Initialize the call history for later assertions."""

        self.calls: list[tuple[str, dict[str, object]]] = []

    async def _call_operation(self, operation_id: str, **kwargs: object) -> str:
        """Record the operation id and arguments instead of sending HTTP."""

        self.calls.append((operation_id, kwargs))
        return operation_id


def test_every_generated_sync_method_calls_the_expected_operation() -> None:
    """All generated sync wrappers should delegate to `_call_operation`."""

    fake_client = RecordingClient()
    for namespace_name, namespace_type in NAMESPACE_REGISTRY.items():
        namespace = namespace_type(fake_client)
        for method_name, method in getmembers(namespace, predicate=ismethod):
            if method_name.startswith("_"):
                continue
            result = method(**build_call_kwargs(method))
            assert isinstance(result, str)
            assert result.startswith(f"{namespace_name}.")
    assert fake_client.calls


def test_every_generated_sync_method_works_without_extra_params() -> None:
    """Generated sync wrappers should also work when `extra_params` is omitted."""

    fake_client = RecordingClient()
    for namespace_type in NAMESPACE_REGISTRY.values():
        namespace = namespace_type(fake_client)
        for method_name, method in getmembers(namespace, predicate=ismethod):
            if method_name.startswith("_"):
                continue
            method(**build_call_kwargs(method, include_extra_params=False))
    assert fake_client.calls


@pytest.mark.asyncio
async def test_every_generated_async_method_calls_the_expected_operation() -> None:
    """All generated async wrappers should delegate to `_call_operation`."""

    fake_client = RecordingAsyncClient()
    for namespace_name, namespace_type in ASYNC_NAMESPACE_REGISTRY.items():
        namespace = namespace_type(fake_client)
        for method_name, method in getmembers(namespace, predicate=ismethod):
            if method_name.startswith("_"):
                continue
            result = await method(**build_call_kwargs(method))
            assert isinstance(result, str)
            assert result.startswith(f"{namespace_name}.")
    assert fake_client.calls


@pytest.mark.asyncio
async def test_every_generated_async_method_works_without_extra_params() -> None:
    """Generated async wrappers should also work when `extra_params` is omitted."""

    fake_client = RecordingAsyncClient()
    for namespace_type in ASYNC_NAMESPACE_REGISTRY.values():
        namespace = namespace_type(fake_client)
        for method_name, method in getmembers(namespace, predicate=ismethod):
            if method_name.startswith("_"):
                continue
            await method(**build_call_kwargs(method, include_extra_params=False))
    assert fake_client.calls


def test_every_generated_model_can_validate_a_minimal_payload() -> None:
    """Generated Pydantic models should accept at least one example-shaped value."""

    for model_name, model_type in MODEL_REGISTRY.items():
        field_payload = {}
        for field_name, field_info in model_type.model_fields.items():
            alias = field_info.alias or field_name
            annotation_text = str(field_info.annotation)
            if "bool" in annotation_text:
                field_payload[alias] = True
            elif "int" in annotation_text:
                field_payload[alias] = 1
            else:
                field_payload[alias] = "example"
            break
        model = model_type.model_validate(field_payload)
        assert model is not None, model_name
