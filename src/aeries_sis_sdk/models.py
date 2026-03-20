"""Shared runtime models used by generated endpoint wrappers.

The generated models inherit from :class:`AeriesModel` so they all allow extra
fields. This matches the project plan: documented fields are typed when known,
but undocumented vendor additions should not break consumers immediately.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict


class AeriesModel(BaseModel):
    """Base model for SDK response objects.

    The Aeries support articles are descriptive rather than machine-perfect, so
    the SDK validates documented fields but permits extra fields by default.
    """

    model_config = ConfigDict(extra="allow")


def parse_payload(model_type: type[AeriesModel], payload: Any) -> Any:
    """Validate dicts and lists of dicts against a generated model type."""

    if isinstance(payload, list):
        return [
            model_type.model_validate(item) if isinstance(item, dict) else item
            for item in payload
        ]
    if isinstance(payload, dict):
        return model_type.model_validate(payload)
    return payload
