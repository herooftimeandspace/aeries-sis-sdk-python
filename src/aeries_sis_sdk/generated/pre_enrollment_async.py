"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class PreEnrollmentAsyncNamespace:
    """Generated namespace for the `pre_enrollment` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    async def pre_enroll_inactive_student(self, student_id: str | int, next_school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Pre-Enroll Inactive Student` endpoint.

        Summary: The Pre-Enroll Inactive Student endpoint provides the ability to create a Pre-Enroll student record from an inactive STU record and place the resulting new pre-enrolled record in a desired school.

        Security area: "Student Data" - Update

        Notes:
        - The Pre-Enroll Inactive Student endpoint provides the ability to create a Pre-Enroll student record from an inactive STU record and place the resulting new pre-enrolled record in a desired school.
        - The {StudentID} value determines which student will be pre-enrolled.
        - The {NewSchoolCode} value determines where the student will be pre-enrolled.
        - A student record must be inactive to be pre-enrolled to another school utilizing this endpoint.

        """
        path_params: dict[str, Any] = {"StudentID": student_id, "NextSchoolCode": next_school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("pre_enrollment.pre_enroll_inactive_student", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def pre_enroll_student(self, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Pre-Enroll Student` endpoint.

        Summary: The Pre-Enroll Student endpoint allows a student to be transferred as a pre-enrolled student to their approved school for the next school year.

        Security area: "Trigger Student Pre-Enrollment" - Insert

        Notes:
        - The Pre-Enroll Student endpoint allows a student to be transferred as a pre-enrolled student to their approved school for the next school year.
        - The NextSchool field of the active record determines where the student will be pre-enrolled.
        - A student record must be active to be pre-enrolled to another school. The system will automatically determine the most recent active record if the student has more than one.
        - Any existing pre-enrolled records for the student at other schools will be deleted. There should only ever be one pre-enrolled record for a student at a given time.

        """
        path_params: dict[str, Any] = {"StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("pre_enrollment.pre_enroll_student", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)
