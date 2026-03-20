"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class SchoolsNamespace:
    """Generated namespace for the `schools` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    def get_absence_codes(self, school_code: str | int, absence_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Absence Codes` endpoint.

        Security area: "Absence Code Table"

        Notes:
        - If Absence Code is not passed, all absence codes for the chosen school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "AbsenceCode": absence_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("schools.get_absence_codes", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_bell_schedule(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Bell Schedule` endpoint.

        Security area: "Bell Schedule"

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("schools.get_bell_schedule", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_bell_schedule_date_date(self, school_code: str | int, date: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Bell Schedule` endpoint.

        Security area: "Bell Schedule"

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "Date": date}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("schools.get_bell_schedule_date_date", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_code_sets(self, table: str | int, field: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Code Sets` endpoint.

        Security area: None Required (certificate in request is still required though)

        Notes:
        - The code set for all field objects whose name ends in "Code" can be looked up using this API End Point.

        """
        path_params: dict[str, Any] = {"Table": table, "Field": field}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("schools.get_code_sets", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_school_calendar(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `School Calendar` endpoint.

        Security area: "Calendar"

        Notes:
        - Pass a School Code of 0 (zero) for the district-level calendar. Not all districts configure a district-level calendar though.
        - Track Holidays might be a blank data element if the School.Tracks field is 0.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("schools.get_school_calendar", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_school_information(self, school_code: str | int | None = None, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `School Information` endpoint.

        Security area: None Required (certificate in request is still required though)

        Notes:
        - If School Code is not passed, all schools for the current district will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("schools.get_school_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_school_terms(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `School Terms` endpoint.

        Security area: None Required (certificate in request is still required though)

        Notes:
        - This information is already available on each school returned from the "School Information" end point.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("schools.get_school_terms", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)
