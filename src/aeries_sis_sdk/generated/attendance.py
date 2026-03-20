"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class AttendanceNamespace:
    """Generated namespace for the `attendance` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    def get_attendance_history_attendance_codes(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Attendance History Attendance Codes` endpoint.

        Security area: "Attendance History"

        Notes:
        - This end point will return a history of Attendance Codes used by the selected school and can be limited to a specific academic year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_attendance_history_attendance_codes", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_attendance_history_attendance_codes_year_year(self, school_code: str | int, year: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Attendance History Attendance Codes` endpoint.

        Security area: "Attendance History"

        Notes:
        - This end point will return a history of Attendance Codes used by the selected school and can be limited to a specific academic year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "year": year}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_attendance_history_attendance_codes_year_year", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_attendance_history_details(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Attendance History Details` endpoint.

        Security area: "Attendance History"

        Notes:
        - This end point will return details of Attendance History data and can be limited to a specific student or to a specific academic year.
        - Passing “SchoolCode” without “StudentID” will limit the results to students who currently have a record in the selected school, but the Attendance History may include data from other schools.
        - Passing “StudentID” will effectively ignore the passed “SchoolCode” and return all Attendance History for the selected student regardless of whether the student is currently in the selected school.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_attendance_history_details", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_attendance_history_details_year_year(self, school_code: str | int, year: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Attendance History Details` endpoint.

        Security area: "Attendance History"

        Notes:
        - This end point will return details of Attendance History data and can be limited to a specific student or to a specific academic year.
        - Passing “SchoolCode” without “StudentID” will limit the results to students who currently have a record in the selected school, but the Attendance History may include data from other schools.
        - Passing “StudentID” will effectively ignore the passed “SchoolCode” and return all Attendance History for the selected student regardless of whether the student is currently in the selected school.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "year": year}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_attendance_history_details_year_year", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_attendance_history_summary(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Attendance History Summary` endpoint.

        Security area: "Attendance History"

        Notes:
        - This end point will return a summary of Attendance History data and can be limited to a specific student or to a specific academic year.
        - Passing “SchoolCode” without “StudentID” will limit the results to students who currently have a record in the selected school, but the Attendance History may include data from other schools.
        - Passing “StudentID” will effectively ignore the passed “SchoolCode” and return all Attendance History for the selected student regardless of whether the student is currently in the selected school.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_attendance_history_summary", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_attendance_history_summary_year_year(self, school_code: str | int, year: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Attendance History Summary` endpoint.

        Security area: "Attendance History"

        Notes:
        - This end point will return a summary of Attendance History data and can be limited to a specific student or to a specific academic year.
        - Passing “SchoolCode” without “StudentID” will limit the results to students who currently have a record in the selected school, but the Attendance History may include data from other schools.
        - Passing “StudentID” will effectively ignore the passed “SchoolCode” and return all Attendance History for the selected student regardless of whether the student is currently in the selected school.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "year": year}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_attendance_history_summary_year_year", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_student_attendance(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Attendance` endpoint.

        Security area: "Attendance"

        Notes:
        - This end point will return detailed student attendance data for the selected school.
        - An “AttendanceDay” is only returned if the student has an attendance code for that day or for at least one period in that day. For negative attendance schools, it is normal for many days to be “missing” from student attendance results because no attendance code is entered when the student is present for the day or period.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_student_attendance", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_student_enrollment_history(self, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Enrollment History` endpoint.

        Security area: "Enrollment History"

        Notes:
        - This end point will return the enrollment history for one or all students. It can be limited to a specific school code and should be limited to a specific academic year.

        """
        path_params: dict[str, Any] = {"StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_student_enrollment_history", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_student_enrollment_history_schools_school_code_enrollment_student_id(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Enrollment History` endpoint.

        Security area: "Enrollment History"

        Notes:
        - This end point will return the enrollment history for one or all students. It can be limited to a specific school code and should be limited to a specific academic year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_student_enrollment_history_schools_school_code_enrollment_student_id", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_student_enrollment_history_schools_school_code_enrollment_student_id_year_academic_year(self, school_code: str | int, student_id: str | int, academic_year: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Enrollment History` endpoint.

        Security area: "Enrollment History"

        Notes:
        - This end point will return the enrollment history for one or all students. It can be limited to a specific school code and should be limited to a specific academic year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id, "AcademicYear": academic_year}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_student_enrollment_history_schools_school_code_enrollment_student_id_year_academic_year", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_student_enrollment_history_year_academic_year(self, student_id: str | int, academic_year: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Enrollment History` endpoint.

        Security area: "Enrollment History"

        Notes:
        - This end point will return the enrollment history for one or all students. It can be limited to a specific school code and should be limited to a specific academic year.

        """
        path_params: dict[str, Any] = {"StudentID": student_id, "AcademicYear": academic_year}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("attendance.get_student_enrollment_history_year_academic_year", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)
