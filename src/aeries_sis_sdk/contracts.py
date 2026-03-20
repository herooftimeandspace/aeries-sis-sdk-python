"""Helpers for loading and matching the committed Aeries contract snapshot."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .contract_types import ContractDocument, ContractOperation

_PACKAGED_CONTRACT_PATH = Path(__file__).with_name("generated") / "contract_snapshot.json"


def load_contract(path: Path | None = None) -> ContractDocument:
    """Load the normalized contract JSON from disk.

    Parameters
    ----------
    path:
        Optional override path that is mainly useful in tests.
    """

    contract_path = path or _PACKAGED_CONTRACT_PATH
    if not contract_path.exists():
        return ContractDocument()
    with contract_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return ContractDocument.model_validate(payload)


def find_operation_by_id(contract: ContractDocument, operation_id: str) -> ContractOperation:
    """Return a contract operation by id or raise a helpful validation error."""

    for operation in contract.operations:
        if operation.operation_id == operation_id:
            return operation
    raise LookupError(f"Unknown contract operation: {operation_id}")


def maybe_match_operation(
    contract: ContractDocument, method: str, path_template: str
) -> ContractOperation | None:
    """Return an operation for the exact method/template pair when available."""

    method = method.upper()
    for operation in contract.operations:
        if operation.method == method and operation.path_template == path_template:
            return operation
    return None


def format_path(
    path_template: str,
    *,
    path_params: dict[str, Any] | None,
    optional_path_parameter_names: set[str] | None = None,
) -> str:
    """Format a contract path template and remove missing optional segments.

    Optional placeholders occur in several Aeries pages where the docs show a
    single template such as `/schools/{SchoolCode}` even though the segment may
    be omitted. We drop a segment only when the whole segment is just a missing
    placeholder, which is the safe case.
    """

    path_params = path_params or {}
    optional_path_parameter_names = optional_path_parameter_names or set()
    pieces: list[str] = []
    for segment in path_template.strip("/").split("/"):
        if segment.startswith("{") and segment.endswith("}"):
            placeholder = segment[1:-1]
            value = path_params.get(placeholder)
            if value in (None, "") and placeholder in optional_path_parameter_names:
                continue
            if value in (None, ""):
                raise ValueError(f"Missing required path parameter: {placeholder}")
            pieces.append(str(value))
            continue
        pieces.append(segment)
    return "/" + "/".join(piece for piece in pieces if piece)


def merge_query_params(
    *,
    params: dict[str, Any] | None,
    database_year: str | int | None,
    default_database_year: str | int | None,
) -> dict[str, Any]:
    """Merge user params with the global DatabaseYear default when needed."""

    merged = dict(params or {})
    chosen_year = database_year if database_year is not None else default_database_year
    if chosen_year is not None and "DatabaseYear" not in merged:
        merged["DatabaseYear"] = str(chosen_year)
    return merged

