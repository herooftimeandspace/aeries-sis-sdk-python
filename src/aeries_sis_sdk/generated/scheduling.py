"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class SchedulingNamespace:
    """Generated namespace for the `scheduling` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    def create_section_from_scheduling_master_schedule(self, school_code: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Section (from Scheduling Master Schedule) ↑` endpoint.

        Security area: "Scheduling Master Schedule"

        Notes:
        - If Section Number is not passed, all section records in the scheduling master schedule of the given school will be returned.
        - After a successful request, this end point returns HTTP status code 201, and the response body contains the "SchedulingMasterScheduleSection" object that was just created.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.create_section_from_scheduling_master_schedule", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    def get_course_data_changes(self, year: str | int, month: str | int, day: str | int, hour: str | int, minute: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Course Data Changes ↑` endpoint.

        Security area: "Course Data"

        """
        path_params: dict[str, Any] = {"year": year, "month": month, "day": day, "hour": hour, "minute": minute}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_course_data_changes", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_course_information(self, course_id: str | int | None = None, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Course Information ↑` endpoint.

        Security area: "Course Data"

        """
        path_params: dict[str, Any] = {"CourseID": course_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_course_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_section_class_roster(self, school_code: str | int, section_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Section Class Roster ↑` endpoint.

        Security area: "Class Schedules/History"

        Notes:
        - This information can also be requested on a student by student basis. See Student Class Schedule End Point.
        - When this information is requested before the beginning of the school year the SequenceNumber and SectionNumber values will match.
        - Be aware that Class Schedules are highly prone to large scale adjustments before the start of school through the first 2 weeks of the school year.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "SectionNumber": section_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_section_class_roster", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_section_class_roster_data_changes(self, year: str | int, month: str | int, day: str | int, hour: str | int, minute: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Section Class Roster Data Changes ↑` endpoint.

        Security area: "Class Schedules/History"

        Notes:
        - This should be used for advanced interfaces with Aeries where you may be pulling data hourly or daily and want to only get the changes since the last time you pulled data from the Aeries API. After you get the list of sections with roster changes, you will have to loop through the dataset and call the Section Class Roster API one record at a time.

        """
        path_params: dict[str, Any] = {"year": year, "month": month, "day": day, "hour": hour, "minute": minute}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_section_class_roster_data_changes", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_section_data_changes_from_master_schedule(self, year: str | int, month: str | int, day: str | int, hour: str | int, minute: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Section Data Changes (from Master Schedule) ↑` endpoint.

        Security area: "Master Schedule"

        Notes:
        - This should be used for advanced interfaces with Aeries where you may be pulling data hourly or daily and want to only get the changes since the last time you pulled data from the Aeries API. After you get the list of sections with changes, you will have to loop through the dataset and call the Section (from Master Schedule) API one record at a time.
        - Example Section (from Master Schedule) Data Changes Results:
        - https://demo.aeries.net/aeries/api/v5/SectionDataChanges/2020/1/1/0/0
        - { "SchoolCode": 884, "SectionNumber": 43 }, { "SchoolCode": 884, "SectionNumber": 44 }, { "SchoolCode": 884, "SectionNumber": 45 }, { "SchoolCode": 884, "SectionNumber": 46 }, { "SchoolCode": 884, "SectionNumber": 47 }, { "SchoolCode": 884, "SectionNumber": 48 }, { "SchoolCode": 884, "SectionNumber": 49 } ... ... }

        """
        path_params: dict[str, Any] = {"year": year, "month": month, "day": day, "hour": hour, "minute": minute}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_section_data_changes_from_master_schedule", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_section_from_scheduling_master_schedule(self, school_code: str | int, section_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Section (from Scheduling Master Schedule) ↑` endpoint.

        Security area: "Scheduling Master Schedule"

        Notes:
        - If Section Number is not passed, all section records in the scheduling master schedule of the given school will be returned.
        - After a successful request, this end point returns HTTP status code 201, and the response body contains the "SchedulingMasterScheduleSection" object that was just created.

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "SectionNumber": section_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_section_from_scheduling_master_schedule", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_sections_from_master_schedule(self, school_code: str | int, section_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Sections (from Master Schedule) ↑` endpoint.

        Security area: "Master Schedule"

        Notes:
        - If Section Number is not passed, all section records in the master schedule of the given school will be returned.
        - Example Section (from Master Schedule) Results:
        - https://demo.aeries.net/aeries/api/v5/schools/994/sections/100
        - { "SchoolCode": 995, "SectionNumber": 100, "Period": "1", "PeriodBlock": 1, "Semester": "Y", "ClassCalendar": "MTWTF", "CourseID": "327", "SectionStaffMembers": [ { "StaffID": 995001, "LastName": "Aldrich", "FirstName": "Darryl", "IsPrimaryTeacher": true, "StaffRoleCode": "", "TeacherPositionCode": "", "AttendancePermission": "", "GradebookPermissionCode": "", "GradeReportingAccess": "", "StudentAccess": "", "IncludeInStateReporting": "", "StartDate": null, "EndDate": null, "InactiveStatusCode": "" }, { "StaffID": 700004321, "LastName": "Carlisle", "FirstName": "Jackie", "IsPrimaryTeacher": false, "StaffRoleCode": "", "TeacherPositionCode": "", "AttendancePermission": "", "GradebookPermissionCode": "", "GradeReportingAccess": "", "StudentAccess": "", "IncludeInStateReporting": "", "StartDate": null, "EndDate": null, "InactiveStatusCode": "I" }, { "StaffID": 700005678, "LastName": "Cullens", "FirstName": "Mary", "IsPrimaryTeacher": false, "StaffRoleCode": "", "TeacherPositionCode": "", "AttendancePermission": "", "GradebookPermissionCode": "R", "GradeReportingAccess": "", "StudentAccess": "", "IncludeInStateReporting": "", "StartDate": null, "EndDate": null, "InactiveStatusCode": "" } ], "Room": "", "Credit": 0.0000, "GenderRestriction": "", "LowGrade": 9, "HighGrade": 12, "MaxStudents": 30, "TotalStudents": 21, "TotalBoys": 14, "TotalGirls": 7, "TotalOtherGender": 0, "InactiveStatusCode": "", "ProgramCode": "", "HourlyAttendanceProgramCode": "", "ExclusionCode": "", "CountsForADA": "", "MultiTeacherCode": "", "SchedulingGroup": "", "TeamCourseGroup": "", "TeamNumber": 0, "SemesterGroup": "", "Track": "", "ClassID": 0, "EducationServiceCode": "", "LanguageOfInstructionCode": "", "InstructionalStrategyCode": "", "FundingSourceCode": "", "CareerTechnicalEducationProviderCode": "", "IndependentStudyIndicator": "", "DistanceLearningIndicator": "", "ItinerantTeacherIndicator": "", "UseSupplementalAttendance": false, "ArticulatedCourseIndicator": "", "NonCampusBasedInstructionCode": "", "PopulationServedCode": "", "ClassTypeCode": "", "MonthlyMinutes": 0, "PreKSchoolTypeCode": "", "PreKCurriculaCode": "", "IsHighQualityPreKProgram": false, "InstructionTypeCode": "", "ProgramEvaluationTypeCode": "", "EducationalEnvironmentCode": "", "CareerTechnicalEducationHours": 0, "ContentSubcategoryCode": "", "CharterNonCoreIndicator": "", "AdvancedCourseStateCode": "", "OnlineInstructionTypeCode": "", "MiddleSchoolCoreIndicator": "", "NonCredentialedAuthorizationCode": "", "HighQualityCareerTechnicalEducationIndicator": "", "UserCode1": "", "UserCode2": "", "UserCode3": "", "UserCode4": "", "UserCode5": "", "UserCode6": "", "UserCode7": "", "UserCode8": "", "PrimaryClass": false }

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "SectionNumber": section_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_sections_from_master_schedule", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_staff_classes_sections(self, staff_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Staff Classes/Sections ↑` endpoint.

        Security area: "Master Schedule"

        Notes:
        - This end point will return a list of classes associated with the given Staff ID.
        - Example Staff Classes/Sections Results:
        - https://demo.aeries.net/aeries/api/v5/staff/994605/classes
        - Note: The results for this end point follow the exact same structure as the Section (from Master Schedule) end point documented above.

        """
        path_params: dict[str, Any] = {"StaffID": staff_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("scheduling.get_staff_classes_sections", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)
