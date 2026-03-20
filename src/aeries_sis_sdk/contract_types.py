"""Typed models that describe the committed Aeries API contract.

These models are used in three places:

1. The contract sync tool writes normalized JSON with them.
2. The generator reads the normalized JSON and emits Python wrappers.
3. The runtime loads the packaged snapshot to make retry and validation choices.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any, Literal

from pydantic import BaseModel, Field


class ContractSource(BaseModel):
    """Describe one upstream article that participates in the SDK contract."""

    key: str
    category: str
    url: str
    article_title: str | None = None
    fetched_at: str | None = None
    content_hash: str | None = None
    raw_path: str | None = None


class ContractParameter(BaseModel):
    """Describe one path or query parameter exposed by an endpoint."""

    name: str
    python_name: str
    location: Literal["path", "query"]
    required: bool
    description: str


class ContractField(BaseModel):
    """Describe one documented field from a field-documentation table."""

    name: str
    python_name: str
    source_column: str | None = None
    description: str
    inferred_type: str = "Any"


class ContractExample(BaseModel):
    """Carry one example snippet or example URL from the upstream docs."""

    label: str
    content: str
    format: Literal["json", "url", "text"] = "text"


class ContractOperation(BaseModel):
    """Describe one callable Aeries endpoint variant."""

    operation_id: str
    category: str
    section_title: str
    python_name: str
    summary: str | None = None
    source_key: str
    source_url: str
    method: Literal["GET", "POST", "PUT", "DELETE"]
    path_template: str
    security_area: str | None = None
    side_effect: bool = False
    response_kind: Literal["unknown", "object", "list", "scalar"] = "unknown"
    response_model_name: str
    path_parameters: list[ContractParameter] = Field(default_factory=list)
    query_parameters: list[ContractParameter] = Field(default_factory=list)
    field_docs: list[ContractField] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    examples: list[ContractExample] = Field(default_factory=list)


class ContractDocument(BaseModel):
    """Represent the whole normalized Aeries contract snapshot."""

    api_version: str = "v5"
    generated_at: str = Field(
        default_factory=lambda: datetime.now(UTC).replace(microsecond=0).isoformat()
    )
    request_defaults: dict[str, Any] = Field(default_factory=dict)
    sources: list[ContractSource] = Field(default_factory=list)
    operations: list[ContractOperation] = Field(default_factory=list)

