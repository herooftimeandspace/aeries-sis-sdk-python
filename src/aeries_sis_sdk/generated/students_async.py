"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class StudentsAsyncNamespace:
    """Generated namespace for the `students` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    async def create_contacts_create(self, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Contacts - Create ↑` endpoint.

        Summary: Security Area:

        Notes:
        - Security Area:
        - "Contacts" – Read & Insert “Contacts” – Field-level Insert permission is required for each field; otherwise, the value will be ignored.
        - This end point returns a single “Contact” object representing the contact record that was just added. For the specification of the “Contact” object, see the Contacts section of the main Aeries API documentation.
        - Any field that is omitted will be assigned the Aeries default value for that field.

        """
        path_params: dict[str, Any] = {"StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.create_contacts_create", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    async def create_student_information_create(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Student Information - Create ↑` endpoint.

        Summary: Security Area:

        Notes:
        - Security Area:
        - "Student Data" – Read & Insert “Student Demographics” – Field-level Insert permission is required for each field; otherwise, the value will be ignored.
        - This end point returns a single “Student” object representing the student record that was just added. For the specification of the “Student” object, see the Student Information section of the main Aeries API documentation.
        - This end point should only be used to create a record for a student who has never been enrolled in the district. It cannot not be used to add or transfer an existing student to a different school.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.create_student_information_create", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    async def create_student_information_update(self, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Student Information - Update ↑` endpoint.

        Security area: "Student Data" – Read & Update

        Notes:
        - This end point returns an array of “Student” objects representing the student record(s) that were updated. The result is an array because the same student ID may have a record at multiple schools, and all will be updated. For the specification of the “Student” object, see the Student Information section of the main Aeries API documentation.
        - Any field that is omitted will NOT be updated in the Aeries database.

        """
        path_params: dict[str, Any] = {"StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.create_student_information_update", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    async def create_update_address(self, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Update Address ↑` endpoint.

        Security area: "Student Data" – Read & Update

        Notes:
        - This end point returns an array of “Student” objects representing the student record(s) that were updated. The result is an array because the same student ID may have a record at multiple schools, and all will be updated. For the specification of the “Student” object, see the Student Information section of the main Aeries API documentation.
        - Any field that is omitted will NOT be updated in the Aeries database.

        """
        path_params: dict[str, Any] = {"StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.create_update_address", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    async def get_assertive_discipline(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Assertive Discipline ↑` endpoint.

        Security area: "Assertive Discipline"

        Notes:
        - This end point will return a full history of all "Assertive Discipline" records for all students in the selected school. This will include incidents from previous school years and those from different schools. An "Assertive Discipline" record normally represents a behavioral incident that resulted in punitive action.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_assertive_discipline", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_college_entrance_test_scores(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `College Entrance Test Scores ↑` endpoint.

        Security area: "College Entrance Tests"

        Notes:
        - This end point will return a full history of all tests normally taken in preparation for college. These include: SAT I, SAT II, ACT, IB, and AP tests.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_college_entrance_test_scores", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_contacts(self, school_code: str | int, student_id: str | int | None = None, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Contacts ↑` endpoint.

        Security area: "Contacts"

        Notes:
        - If Student ID is not passed, all student contacts for the given school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_contacts", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_discipline(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Discipline ↑` endpoint.

        Security area: "Discipline"

        Notes:
        - This end point will return a full history of all "Discipline" records for all students in the selected school. This will include incidents from previous school years and those from different schools. An "Discipline" record normally represents minor infractions (less severe offenses) for a student.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_discipline", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_district_supplemental_student_data(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `District Supplemental Student Data ↑` endpoint.

        Security area: "District Supplemental Data"

        Notes:
        - This end point will return student information from the "DSD" table in Aeries. This is a table that can be customized by each district with a set of fields that are consistent for all instances of a student record throughout the district (when the student is enrolled in multiple schools during the year).

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_district_supplemental_student_data", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_fees_and_fines(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Fees and Fines ↑` endpoint.

        Security area: "Fees and Fines"

        Notes:
        - This end point will return a full history of all fees and fines incurred by the student, including those that have already been paid.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_fees_and_fines", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_programs(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Programs ↑` endpoint.

        Security area: "Student Programs"

        Notes:
        - If Student ID is not passed and you pass a 0 (zero) instead, all programs for the given school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_programs", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_school_supplemental_student_data(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `School Supplemental Student Data ↑` endpoint.

        Security area: "Supplemental Data"

        Notes:
        - This end point will return student information from the "SUP" table in Aeries. This is a table that can be customized by each district with a set of fields whose values are unique for each school a student is enrolled.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_school_supplemental_student_data", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_data_changes(self, data_area: str | int, year: str | int, month: str | int, day: str | int, hour: str | int, minute: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Data Changes ↑` endpoint.

        Security area: "Student Data"

        Notes:
        - This should be used for advanced interfaces with Aeries where you may be pulling data hourly or daily and want to only get the changes since the last time you pulled data from the Aeries API. After you get the list of students with changes in the given data area, you will have to loop through the corresponding API to pull the new records one student at a time.

        """
        path_params: dict[str, Any] = {"DataArea": data_area, "year": year, "month": month, "day": day, "hour": hour, "minute": minute}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_data_changes", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_groups(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Groups` endpoint.

        Security area: "Student Groups"

        Notes:
        - Student Groups are lists of students that schools have grouped together for any purpose, such as athletic team membership, club participation, academic reasons, special programs, etc.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_groups", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_information(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Information` endpoint.

        Security area: "Student Data"

        Notes:
        - If Student ID is not passed, all students for the given school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_information_extended(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Information Extended ↑` endpoint.

        Security area: "Student Data"

        Notes:
        - If 0 is passed for Student ID, all students for the given school will be returned.
        - Results are always returned in the form of an "Array of Student Extended" because often students have multiple records in a district if they are concurrently enrolled or have switched between schools during the school year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_information_extended", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_information_extended_grade_grade_level_extended(self, school_code: str | int, grade_level: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Information Extended ↑` endpoint.

        Security area: "Student Data"

        Notes:
        - If 0 is passed for Student ID, all students for the given school will be returned.
        - Results are always returned in the form of an "Array of Student Extended" because often students have multiple records in a district if they are concurrently enrolled or have switched between schools during the school year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "GradeLevel": grade_level}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_information_extended_grade_grade_level_extended", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_information_extended_sn_student_number_extended(self, school_code: str | int, student_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Information Extended ↑` endpoint.

        Security area: "Student Data"

        Notes:
        - If 0 is passed for Student ID, all students for the given school will be returned.
        - Results are always returned in the form of an "Array of Student Extended" because often students have multiple records in a district if they are concurrently enrolled or have switched between schools during the school year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentNumber": student_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_information_extended_sn_student_number_extended", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_information_grade_grade_level(self, school_code: str | int, grade_level: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Information` endpoint.

        Security area: "Student Data"

        Notes:
        - If Student ID is not passed, all students for the given school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "GradeLevel": grade_level}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_information_grade_grade_level", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_information_sn_student_number(self, school_code: str | int, student_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Information` endpoint.

        Security area: "Student Data"

        Notes:
        - If Student ID is not passed, all students for the given school will be returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentNumber": student_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_information_sn_student_number", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_student_picture(self, school_code: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Student Picture ↑` endpoint.

        Security area: "Student Pictures"

        Notes:
        - This end point will return the most recent photo of the student stored in Aeries.
        - Due to the large amount of data that this end point may return, it is HIGHLY recommended to use either an individual student ID or query string filters to limit the number of records returned.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_student_picture", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_test_scores(self, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Test Scores ↑` endpoint.

        Security area: "Test Scores"

        Notes:
        - This end point will return a full history of all State and locally administered Standardized Tests in Aeries. Examples include SBAC (CAASPP) and ELPAC. College Entrance Test Scores such as SAT I, SAT II, ACT, IB, and AP are available in a separate area detailed elsewhere in this documentation.

        """
        path_params: dict[str, Any] = {"StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_test_scores", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    async def get_update_test_scores(self, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Update Test Scores ↑` endpoint.

        Security area: "Test Scores" - Update

        Notes:
        - If an existing record is found matched on Student ID, Test ID, Test Part, and Testing Administration, it will be updated. Otherwise, a new record will be added.
        - This end point returns an “ArrayOfTest” container of “Test” objects similar to the regular Test Scores end point; however, it contains only those records which were added or updated by the current Update request.

        """
        path_params: dict[str, Any] = {}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return await self._client._call_operation("students.get_update_test_scores", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)
