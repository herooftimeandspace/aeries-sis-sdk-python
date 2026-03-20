"""Unit tests for the identifier helpers used by generation."""

from __future__ import annotations

from aeries_sis_sdk.naming import pascal_case, snake_case, unique_name


def test_snake_case_handles_acronyms_cleanly() -> None:
    """Acronyms like StudentID should become natural Python names."""

    assert snake_case("StudentID") == "student_id"
    assert snake_case("API Version") == "api_version"


def test_pascal_case_builds_class_names() -> None:
    """PascalCase helpers should be stable for generated class names."""

    assert pascal_case("school information response") == "SchoolInformationResponse"


def test_unique_name_appends_suffixes() -> None:
    """Duplicate generated names should receive numeric suffixes."""

    seen: set[str] = set()
    assert unique_name("value", seen) == "value"
    assert unique_name("value", seen) == "value_2"


def test_snake_case_handles_empty_and_keyword_values() -> None:
    """Empty and keyword-like values should still become safe identifiers."""

    assert snake_case("") == "value"
    assert snake_case("class") == "class_value"
    assert snake_case("123Code") == "value_123_code"
