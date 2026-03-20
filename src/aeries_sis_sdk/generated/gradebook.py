"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

class GradebookNamespace:
    """Generated namespace for the `gradebook` Aeries API group."""

    def __init__(self, client: Any) -> None:
        """Store the parent client used to perform requests."""
        self._client = client

    def create_inserting_a_new_assignment(self, gradebook_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Inserting a New Assignment ↑` endpoint.

        Security area: "Gradebook Data" - Update

        Notes:
        - This end point returns an “ArrayOfAssignment” container of “Assignment” objects similar to the regular Assignment Information end point; however, it contains only those records which were added by the current Insert request. The result is an array because the new Assignment will be added in all Linked Gradebooks if the CreateInLinkedGradebooksToo option is set to “true” or omitted (defaults to “true”). Linked Gradebooks are all a teacher’s Gradebooks in the same school code with equal, nonzero values for “LinkedGroup” (see the Gradebook Information end point)

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.create_inserting_a_new_assignment", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    def create_updating_assignment_scores(self, gradebook_number: str | int, assignment_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Updating Assignment Scores ↑` endpoint.

        Security area: "Gradebook Scores" - Update

        Notes:
        - This end point returns an “ArrayOfAssignmentScore” container of “AssignmentScore” objects similar to the regular Assignment Scores end point. Regardless of how many scores are updated, all scores for the selected assignment will be returned after the update is completed.
        - For Standards-based grades, the list of standards and the "Academic Benchmark Id" are available through the Assignment Information API.
        - For Rubric-based grades, send the numeric Rubric value for Number Correct.

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number, "AssignmentNumber": assignment_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.create_updating_assignment_scores", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    def create_updating_assignment_scores_assignments_unique_id_scores(self, unique_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Updating Assignment Scores ↑` endpoint.

        Security area: "Gradebook Scores" - Update

        Notes:
        - This end point returns an “ArrayOfAssignmentScore” container of “AssignmentScore” objects similar to the regular Assignment Scores end point. Regardless of how many scores are updated, all scores for the selected assignment will be returned after the update is completed.
        - For Standards-based grades, the list of standards and the "Academic Benchmark Id" are available through the Assignment Information API.
        - For Rubric-based grades, send the numeric Rubric value for Number Correct.

        """
        path_params: dict[str, Any] = {"UniqueID": unique_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.create_updating_assignment_scores_assignments_unique_id_scores", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    def get_assignment_information(self, gradebook_number: str | int, assignment_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Assignment Information ↑` endpoint.

        Security area: "Gradebook Data"

        Notes:
        - A method of retrieving assignments for ALL gradebooks for a school or district is not possible. It is recommended that this API be called on the fly when needed by your system to generate a user interface.
        - If AssignmentNumber or UniqueID is passed, a single “Assignment” object is returned rather than an “ArrayOfAssignment”.

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number, "AssignmentNumber": assignment_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_assignment_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_assignment_information_assignments_unique_id(self, unique_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Assignment Information ↑` endpoint.

        Security area: "Gradebook Data"

        Notes:
        - A method of retrieving assignments for ALL gradebooks for a school or district is not possible. It is recommended that this API be called on the fly when needed by your system to generate a user interface.
        - If AssignmentNumber or UniqueID is passed, a single “Assignment” object is returned rather than an “ArrayOfAssignment”.

        """
        path_params: dict[str, Any] = {"UniqueID": unique_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_assignment_information_assignments_unique_id", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_assignment_scores(self, gradebook_number: str | int, assignment_number: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Assignment Scores ↑` endpoint.

        Security area: "Gradebook Scores"

        Notes:
        - A method of retrieving scores for ALL assignments in a gradebook is not possible. It is recommended that this API be called on the fly when needed by your system.
        - For Standards-based grades, the list of standards and the "Academic Benchmark Id" is available through the Assignment Information API.
        - Also for Standards-based grades, the Number Correct and Points Earned fields will always match.
        - For Rubric-based grades, the Number Correct Possible and Points Possible fields will be 0 (zero). Also, the Number Correct and Points Earned fields will match.

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number, "AssignmentNumber": assignment_number, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_assignment_scores", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_assignment_scores_assignments_unique_id_scores_student_id(self, unique_id: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Assignment Scores ↑` endpoint.

        Security area: "Gradebook Scores"

        Notes:
        - A method of retrieving scores for ALL assignments in a gradebook is not possible. It is recommended that this API be called on the fly when needed by your system.
        - For Standards-based grades, the list of standards and the "Academic Benchmark Id" is available through the Assignment Information API.
        - Also for Standards-based grades, the Number Correct and Points Earned fields will always match.
        - For Rubric-based grades, the Number Correct Possible and Points Possible fields will be 0 (zero). Also, the Number Correct and Points Earned fields will match.

        """
        path_params: dict[str, Any] = {"UniqueID": unique_id, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_assignment_scores_assignments_unique_id_scores_student_id", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_final_mark_ranges(self, gradebook_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Final Mark Ranges ↑` endpoint.

        Security area: "Gradebook Data"

        Notes:
        - A method of retrieving final marks for ALL gradebooks for a school or district is not possible. It is recommended that this API be called on the fly when needed by your system.
        - In Aeries, the "Low Value" is used as a threshold. The "High Value" is informational only, except that if the High Value is 0 (zero), then the Final Mark is not being used.

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_final_mark_ranges", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_gradebook_information(self, staff_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Gradebook Information` endpoint.

        Security area: "Gradebook Data"

        Notes:
        - A method of retrieving ALL gradebooks for a school or district is not possible. It is recommended that this API be called on the fly when needed by your system to generate a user interface.
        - Documentation on the Aeries Gradebook can be found here

        """
        path_params: dict[str, Any] = {"StaffID": staff_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_gradebook_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_gradebook_information_gradebooks_gradebook_number(self, gradebook_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Gradebook Information` endpoint.

        Security area: "Gradebook Data"

        Notes:
        - A method of retrieving ALL gradebooks for a school or district is not possible. It is recommended that this API be called on the fly when needed by your system to generate a user interface.
        - Documentation on the Aeries Gradebook can be found here

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_gradebook_information_gradebooks_gradebook_number", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_gradebook_information_schools_school_code_sections_section_number_gradebooks(self, school_code: str | int, section_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Gradebook Information` endpoint.

        Security area: "Gradebook Data"

        Notes:
        - A method of retrieving ALL gradebooks for a school or district is not possible. It is recommended that this API be called on the fly when needed by your system to generate a user interface.
        - Documentation on the Aeries Gradebook can be found here

        """
        path_params: dict[str, Any] = {"SchoolCode": school_code, "SectionNumber": section_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_gradebook_information_schools_school_code_sections_section_number_gradebooks", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def get_gradebook_student_information(self, gradebook_number: str | int, gradebook_term: str | int, student_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None) -> Any:
        """Call the Aeries `Gradebook Student Information ↑` endpoint.

        Security area: "Gradebook Data"

        Notes:
        - A method of retrieving students for ALL gradebooks for a school or district is not possible. It is recommended that this API be called on the fly when needed by your system.
        - Also not available at this time is the ability to request a set of gradebooks for a specific student. This will be available in a future enhancement.

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number, "GradebookTerm": gradebook_term, "StudentID": student_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.get_gradebook_student_information", path_params=path_params, params=params, headers=headers, database_year=database_year, timeout=timeout)

    def update_updating_assignment_information(self, gradebook_number: str | int, assignment_number: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Updating Assignment Information ↑` endpoint.

        Security area: "Gradebook Data" - Update

        Notes:
        - This end point returns an “ArrayOfAssignment” container of “Assignment” objects similar to the regular Assignment Information end point; however, it contains only those records which were updated by the current Update request. The result is an array because the Assignment with the same Assignment Number will be updated in all Linked Gradebooks if the UpdateLinkedGradebooksToo option is set to “true” or omitted (defaults to “true”). Linked Gradebooks are all a teacher’s Gradebooks in the same school code with equal, nonzero values for “LinkedGroup” (see the Gradebook Information end point)

        """
        path_params: dict[str, Any] = {"GradebookNumber": gradebook_number, "AssignmentNumber": assignment_number}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.update_updating_assignment_information", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)

    def update_updating_assignment_information_assignments_unique_id(self, unique_id: str | int, *, headers: Mapping[str, str] | None = None, database_year: str | int | None = None, timeout: float | None = None, extra_params: dict[str, Any] | None = None, json: Any = None) -> Any:
        """Call the Aeries `Updating Assignment Information ↑` endpoint.

        Security area: "Gradebook Data" - Update

        Notes:
        - This end point returns an “ArrayOfAssignment” container of “Assignment” objects similar to the regular Assignment Information end point; however, it contains only those records which were updated by the current Update request. The result is an array because the Assignment with the same Assignment Number will be updated in all Linked Gradebooks if the UpdateLinkedGradebooksToo option is set to “true” or omitted (defaults to “true”). Linked Gradebooks are all a teacher’s Gradebooks in the same school code with equal, nonzero values for “LinkedGroup” (see the Gradebook Information end point)

        """
        path_params: dict[str, Any] = {"UniqueID": unique_id}
        params: dict[str, Any] = {}
        if extra_params:
            params.update(extra_params)
        return self._client._call_operation("gradebook.update_updating_assignment_information_assignments_unique_id", path_params=path_params, params=params, json=json, headers=headers, database_year=database_year, timeout=timeout)
