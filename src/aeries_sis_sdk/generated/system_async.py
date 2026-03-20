"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class SystemAsyncNamespace:
    """Generated namespace for the `system` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    async def get_aeries_installation_information(self, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Aeries Installation Information` endpoint.

        Security area: None required

        """
        path_params: dict[str, Any] = {}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("system.get_aeries_installation_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)
