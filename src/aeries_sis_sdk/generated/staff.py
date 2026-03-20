"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class StaffNamespace:
    """Generated namespace for the `staff` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    def create_staff_information_create(self, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Staff Information - Create ↑` endpoint.

        Summary: Security Area:

        Notes:
        - Security Area:
        - "Staff Data" - Insert
        - After a successful request, this end point returns HTTP status code 201, and the response body contains the "Staff" object that was just created.

        """
        path_params: dict[str, Any] = {}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("staff.create_staff_information_create", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    def get_staff_information(self, staff_id: str | int | None = None, hrid: str | int | None = None, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Staff Information` endpoint.

        Security area: "Staff Data"

        Notes:
        - If Staff ID is not passed, all staff records in the district will be returned.
        - If the API Security Option, Exclude Expire Accounts for Staff Data, is enabled, expired User (UGN) accounts will not be included in the results.

        """
        path_params: dict[str, Any] = {"StaffID": staff_id, "HRID": hrid}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("staff.get_staff_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def update_staff_information_update(self, staff_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Staff Information - Update ↑` endpoint.

        Summary: Security Area:

        Notes:
        - Security Area:
        - "Staff Data" - Update
        - If the Staff ID does not exist, a new record will be created unless the customer has enabled the option to auto-generate new staff IDs. In this case, an error will be generated if the given Staff ID does not already exist.
        - After a successful request, this end point returns the "Staff" object that was just updated or created. If an existing record was updated, the status code will be 200. If a new record was created, the status code will be 201.

        """
        path_params: dict[str, Any] = {"StaffID": staff_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("staff.update_staff_information_update", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)
