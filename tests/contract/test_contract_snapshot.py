"""Tests for the committed contract and generated inventory."""

from __future__ import annotations

from pathlib import Path

from aeries_sis_sdk.contracts import load_contract
from aeries_sis_sdk.generated import OPERATION_INVENTORY
from aeries_sis_sdk.generated.models import MODEL_REGISTRY

ROOT = Path(__file__).resolve().parents[2]


def test_raw_html_snapshots_exist_for_all_sources() -> None:
    """The repo should keep the fetched Aeries article HTML for offline tests."""

    raw_files = sorted((ROOT / "contracts" / "raw").glob("*.html"))
    assert len(raw_files) == 11


def test_contract_snapshot_contains_expected_operations() -> None:
    """Key operations from the plan should exist in the normalized contract."""

    contract = load_contract()
    operation_ids = {operation.operation_id for operation in contract.operations}
    assert "system.get_aeries_installation_information" in operation_ids
    assert "pre_enrollment.pre_enroll_student" in operation_ids
    assert "schools.get_school_information" in operation_ids


def test_generated_inventory_matches_contract_size() -> None:
    """The generated operation inventory should mirror the normalized contract."""

    contract = load_contract()
    assert len(OPERATION_INVENTORY) == len(contract.operations)


def test_generated_model_registry_covers_all_operations() -> None:
    """Each operation should point at a generated response model class."""

    contract = load_contract()
    model_names = {operation.response_model_name for operation in contract.operations}
    assert model_names <= set(MODEL_REGISTRY)

