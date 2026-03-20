"""Naming helpers used by the contract parser and code generator.

The project turns prose-heavy Aeries article headings into Python identifiers.
These helpers centralize that translation so the generator, runtime, and tests
all agree on the same naming rules.
"""

from __future__ import annotations

import keyword
import re

_NON_IDENTIFIER_PATTERN = re.compile(r"[^0-9A-Za-z]+")
_FIRST_CAMEL_PATTERN = re.compile(r"(.)([A-Z][a-z]+)")
_SECOND_CAMEL_PATTERN = re.compile(r"([a-z0-9])([A-Z])")


def snake_case(value: str) -> str:
    """Convert free-form text into a safe Python-style snake_case name."""

    value = value.strip().replace("/", " ").replace("&", " and ")
    value = _FIRST_CAMEL_PATTERN.sub(r"\1_\2", value)
    value = _SECOND_CAMEL_PATTERN.sub(r"\1_\2", value)
    value = _NON_IDENTIFIER_PATTERN.sub("_", value)
    value = value.strip("_").lower()
    if not value:
        return "value"
    if value[0].isdigit():
        value = f"value_{value}"
    if keyword.iskeyword(value):
        value = f"{value}_value"
    return value


def pascal_case(value: str) -> str:
    """Convert free-form text into a PascalCase class name."""

    parts = [part for part in snake_case(value).split("_") if part]
    if not parts:
        return "Value"
    return "".join(part.capitalize() for part in parts)


def unique_name(base_name: str, seen: set[str]) -> str:
    """Return a stable unique name by appending a numeric suffix when needed."""

    candidate = base_name
    index = 2
    while candidate in seen:
        candidate = f"{base_name}_{index}"
        index += 1
    seen.add(candidate)
    return candidate
