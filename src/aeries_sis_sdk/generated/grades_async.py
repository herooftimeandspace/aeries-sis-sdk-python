"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class GradesAsyncNamespace:
    """Generated namespace for the `grades` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    async def get_school_graduation_requirements(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `School Graduation Requirements ↑` endpoint.

        Security area: "Graduation Requirements"

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_school_graduation_requirements", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_school_report_card_marking_periods(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `School Report Card Marking Periods ↑` endpoint.

        Security area: "Grades"

        Notes:
        - This end point returns information about each Report Card Marking Period for the school and can be used to cross-reference with the “MarkingPeriod” number from the Student Report Cards API

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_school_report_card_marking_periods", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_gp_as(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student GPAs` endpoint.

        Security area: "Student Data"

        Notes:
        - If Student ID is not passed, all students for the given school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_student_gp_as", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_grades(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Grades ↑` endpoint.

        Security area: "Grades"

        Notes:
        - This end point allows POST to the following fields only for records that already existing in the Grades (GRD) table: Grade Marks: GRD.M1 - M12 Comments ( GRD.C1 -C3) Citizenship: (GRD.CI) Work Habits: GRD.WH
        - Current Mark Restriction - The API enforces restrictions based on the current marking period ( LOC.TM ): Comment1-3, Citizenship, WorkHabits : Only updated when the requested MarkNumber matches the current marking period The Completion Status ( GRD.TG ): Only calculated/updated for the current marking period Historical Marks: Mark values (M1-M12) can still be updated for any valid marking period
        - Validation Rules Single Mark Per Request Item: Only one mark field (M1-M12) can be updated per student object. If multiple marks are provided, the request will be rejected with a validation error. MarkNumber must be between 1-12 and configured in GRP table for the school Mark Validation (M1-M12): Validates against GRC table (SC, MK, DEL=0). Empty marks allowed. Comment Validation (C1-C3): Validates against COD table (TC='GRD', FC='C1'/'C2'/'C3', DEL=0) Citizenship/Work Habits (CI, WH): Validates against COD table (TC='GRD', FC='CI'/'WH', DEL=0) Related Endpoints Endpoint Description POST /api/v5/schools/{sc}/grades Update grade reporting data (requires valid marks from this endpoint)

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_student_grades", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_graduation_status_summary(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Graduation Status Summary ↑` endpoint.

        Security area: "Graduation Status"

        Notes:
        - If StudentID is not passed, all students in the selected school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_student_graduation_status_summary", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_graduation_status_summary_grade_grade_level(self, school_code: str | int, grade_level: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Graduation Status Summary ↑` endpoint.

        Security area: "Graduation Status"

        Notes:
        - If StudentID is not passed, all students in the selected school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "GradeLevel": grade_level}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_student_graduation_status_summary_grade_grade_level", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_report_cards(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Report Cards ↑` endpoint.

        Security area: "Grades"

        Notes:
        - If Student ID is not passed, all students for the given school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_student_report_cards", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_transcripts(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Transcripts ↑` endpoint.

        Security area: "Transcripts"

        Notes:
        - If StudentID is not passed, all students in the selected school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_student_transcripts", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_valid_marks(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Valid Marks ↑` endpoint.

        Security area: "Grade Reporting: Valid Marks"

        Notes:
        - This end point retrieves the Valid Marks (Grade Codes) from the GRC table
        - Related Endpoints Endpoint Description POST /api/v5/schools/{sc}/grades Update grade reporting data (requires valid marks from this endpoint)

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("grades.get_valid_marks", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)
