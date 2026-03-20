"""Shared pytest helpers for the Aeries SIS SDK test suite."""

from __future__ import annotations

import inspect
from typing import Any


def sample_value(parameter_name: str) -> Any:
    """Return a stable sample value for a generated method parameter."""

    lowered = parameter_name.lower()
    if "school" in lowered:
        return 994
    if "student" in lowered:
        return 99400001
    if "staff" in lowered:
        return 99123
    if "section" in lowered:
        return 1201
    if "gradebook" in lowered:
        return 1001
    if "assignment" in lowered:
        return 12
    if "date" in lowered:
        return "20240101"
    if "year" in lowered:
        return "2024-2025"
    if "month" in lowered:
        return 1
    if "day" in lowered:
        return 2
    if "hour" in lowered:
        return 3
    if "minute" in lowered:
        return 4
    if "json" in lowered:
        return {"example": True}
    return "example"


def build_call_kwargs(callable_object: Any, *, include_extra_params: bool = True) -> dict[str, Any]:
    """Build keyword arguments for a generated method from its signature."""

    kwargs: dict[str, Any] = {}
    signature = inspect.signature(callable_object)
    for name, parameter in signature.parameters.items():
        if name in {"self", "headers", "database_year", "timeout"}:
            continue
        if parameter.kind is inspect.Parameter.VAR_KEYWORD:
            continue
        if name == "extra_params":
            if include_extra_params:
                kwargs[name] = {"ExampleFilter": "value"}
            continue
        if parameter.default is inspect.Signature.empty:
            kwargs[name] = sample_value(name)
            continue
        if name == "json":
            kwargs[name] = {"example": True}
    return kwargs
