"""Opt-in live smoke tests for a real Aeries tenant."""

from __future__ import annotations

import os

import pytest

from aeries_sis_sdk import Client


@pytest.mark.live
def test_live_system_info_smoke() -> None:
    """Call the system-info endpoint when live credentials are available."""

    base_url = os.getenv("AERIES_TEST_BASE_URL")
    certificate = os.getenv("AERIES_TEST_CERT")
    if not base_url or not certificate:
        pytest.skip("AERIES_TEST_BASE_URL and AERIES_TEST_CERT are required for live tests.")

    client = Client(base_url=base_url, certificate=certificate)
    result = client.system.get_aeries_installation_information()
    client.close()

    assert result is not None
