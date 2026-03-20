"""Generate endpoint namespaces and response models from the normalized contract."""

from __future__ import annotations

import json
from pathlib import Path

from aeries_sis_sdk.contract_types import (
    ContractDocument,
    ContractField,
    ContractOperation,
)
from aeries_sis_sdk.naming import pascal_case

ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = ROOT / "src" / "aeries_sis_sdk"

CONTRACT_PATH = ROOT / "contracts" / "normalized" / "aeries_api_contract.json"
GENERATED_DIR = SRC_ROOT / "generated"
HEADER = '''"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""
'''


def load_contract() -> ContractDocument:
    """Load the normalized contract used for code generation."""

    payload = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    return ContractDocument.model_validate(payload)


def python_type(field: ContractField) -> str:
    """Return a conservative Python annotation string for one field."""

    inferred = field.inferred_type or "Any"
    if "|" in inferred:
        return f"{inferred} | None"
    return f"{inferred} | None"


def render_model(operation: ContractOperation) -> str:
    """Render one generated Pydantic model class."""

    lines = [
        f"class {operation.response_model_name}(AeriesModel):",
        f'    """Response model for `{operation.operation_id}`."""',
    ]
    if not operation.field_docs:
        lines.append("    pass")
        return "\n".join(lines)
    seen_fields: set[str] = set()
    for field in operation.field_docs:
        if field.python_name in seen_fields:
            continue
        seen_fields.add(field.python_name)
        description = field.description.replace('"', "'")
        lines.append(
            f"    {field.python_name}: {python_type(field)} = Field("
            f'default=None, alias="{field.name}", description="{description}")'
        )
    return "\n".join(lines)


def docstring_lines(operation: ContractOperation) -> list[str]:
    """Build readable method docstrings from contract metadata."""

    lines = [f'        """Call the Aeries `{operation.section_title}` endpoint.', ""]
    if operation.summary:
        lines.append(f"        Summary: {operation.summary}")
        lines.append("")
    if operation.security_area:
        lines.append(f"        Security area: {operation.security_area}")
        lines.append("")
    if operation.notes:
        lines.append("        Notes:")
        for note in operation.notes[:4]:
            lines.append(f"        - {note}")
        lines.append("")
    lines.append('        """')
    return lines


def signature_for_operation(
    operation: ContractOperation, *, async_mode: bool
) -> tuple[str, dict[str, str]]:
    """Return the method signature and param mapping for one operation."""

    signature_parts = ["self"]
    param_mapping: dict[str, str] = {}
    for parameter in operation.path_parameters + operation.query_parameters:
        annotation = "str | int | None" if not parameter.required else "str | int"
        default = " = None" if not parameter.required else ""
        signature_parts.append(f"{parameter.python_name}: {annotation}{default}")
        param_mapping[parameter.name] = parameter.python_name
    signature_parts.extend(
        [
            "*",
            "headers: Mapping[str, str] | None = None",
            "database_year: str | int | None = None",
            "timeout: float | None = None",
            "extra_params: dict[str, Any] | None = None",
        ]
    )
    if operation.method in {"POST", "PUT", "DELETE"} or operation.side_effect:
        signature_parts.append("json: Any = None")
    signature = ", ".join(signature_parts)
    return signature, param_mapping


def render_method(operation: ContractOperation, *, async_mode: bool) -> str:
    """Render one namespace method for either the sync or async wrapper."""

    signature, param_mapping = signature_for_operation(operation, async_mode=async_mode)
    path_params = {
        parameter.name: param_mapping[parameter.name]
        for parameter in operation.path_parameters
    }
    query_params = {
        parameter.name: param_mapping[parameter.name]
        for parameter in operation.query_parameters
    }
    await_keyword = "await " if async_mode else ""
    path_params_literal = ", ".join(
        f'"{name}": {value}' for name, value in path_params.items()
    )
    query_params_literal = ", ".join(
        f'"{name}": {value}' for name, value in query_params.items()
    )
    lines = [
        f"    {'async ' if async_mode else ''}def {operation.python_name}"
        f"({signature}) -> Any:"
    ]
    lines.extend(docstring_lines(operation))
    lines.append(
        f"        path_params: dict[str, Any] = {{{path_params_literal}}}"
        if path_params
        else "        path_params: dict[str, Any] = {}"
    )
    lines.append(
        f"        params: dict[str, Any] = {{{query_params_literal}}}"
        if query_params
        else "        params: dict[str, Any] = {}"
    )
    lines.append("        if extra_params:")
    lines.append("            params.update(extra_params)")
    lines.append(
        f'        return {await_keyword}self._client._call_operation('
        f'"{operation.operation_id}", '
        "path_params=path_params, "
        "params=params, "
        + (
            "json=json, "
            if operation.method in {"POST", "PUT", "DELETE"} or operation.side_effect
            else ""
        )
        + "headers=headers, database_year=database_year, timeout=timeout)"
    )
    return "\n".join(lines)


def render_namespace(
    category: str, operations: list[ContractOperation], *, async_mode: bool
) -> str:
    """Render one generated namespace module."""

    class_name = f"{pascal_case(category)}{'Async' if async_mode else ''}Namespace"
    lines = [
        HEADER,
        "from __future__ import annotations",
        "",
        "from collections.abc import Mapping",
        "from typing import Any",
        "",
    ]
    lines.append(f"class {class_name}:")
    lines.append(f'    """Generated namespace for the `{category}` Aeries API group."""')
    lines.append("")
    lines.append("    def __init__(self, client: Any) -> None:")
    lines.append('        """Store the parent client used to perform requests."""')
    lines.append("        self._client = client")
    lines.append("")
    for operation in operations:
        lines.append(render_method(operation, async_mode=async_mode))
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_models(operations: list[ContractOperation]) -> None:
    """Write the generated response-model registry."""

    lines = [
        HEADER,
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from pydantic import Field",
        "",
        "from ..models import AeriesModel",
        "",
    ]
    seen: set[str] = set()
    for operation in operations:
        if operation.response_model_name in seen:
            continue
        seen.add(operation.response_model_name)
        lines.append(render_model(operation))
        lines.append("")
    lines.append("MODEL_REGISTRY: dict[str, type[AeriesModel]] = {")
    for operation in operations:
        lines.append(f'    "{operation.response_model_name}": {operation.response_model_name},')
    lines.append("}")
    (GENERATED_DIR / "models.py").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_inventory(categories: dict[str, list[ContractOperation]]) -> None:
    """Write generated namespace exports and the operation inventory."""

    lines = [HEADER, "from __future__ import annotations", ""]
    for category in sorted(categories):
        class_name = f"{pascal_case(category)}Namespace"
        async_class_name = f"{pascal_case(category)}AsyncNamespace"
        lines.append(f"from .{category} import {class_name}")
        lines.append(f"from .{category}_async import {async_class_name}")
    lines.append("")
    lines.append("NAMESPACE_REGISTRY = {")
    for category in sorted(categories):
        class_name = f"{pascal_case(category)}Namespace"
        lines.append(f'    "{category}": {class_name},')
    lines.append("}")
    lines.append("")
    lines.append("ASYNC_NAMESPACE_REGISTRY = {")
    for category in sorted(categories):
        async_class_name = f"{pascal_case(category)}AsyncNamespace"
        lines.append(f'    "{category}": {async_class_name},')
    lines.append("}")
    lines.append("")
    lines.append("OPERATION_INVENTORY = {")
    for operations in categories.values():
        for operation in operations:
            lines.append(f'    "{operation.operation_id}": "{operation.path_template}",')
    lines.append("}")
    (GENERATED_DIR / "__init__.py").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    """Entry point for generating Python code from the normalized contract."""

    contract = load_contract()
    categories: dict[str, list[ContractOperation]] = {}
    for operation in contract.operations:
        categories.setdefault(operation.category, []).append(operation)
    write_models(contract.operations)
    for category, operations in categories.items():
        operations = sorted(operations, key=lambda item: item.operation_id)
        (GENERATED_DIR / f"{category}.py").write_text(
            render_namespace(category, operations, async_mode=False),
            encoding="utf-8",
        )
        (GENERATED_DIR / f"{category}_async.py").write_text(
            render_namespace(category, operations, async_mode=True),
            encoding="utf-8",
        )
    write_inventory(categories)
    print(f"Generated SDK namespaces for {len(categories)} categories.")


if __name__ == "__main__":
    main()
