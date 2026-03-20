"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations

from .attendance import AttendanceNamespace
from .attendance_async import AttendanceAsyncNamespace
from .gradebook import GradebookNamespace
from .gradebook_async import GradebookAsyncNamespace
from .grades import GradesNamespace
from .grades_async import GradesAsyncNamespace
from .pre_enrollment import PreEnrollmentNamespace
from .pre_enrollment_async import PreEnrollmentAsyncNamespace
from .scheduling import SchedulingNamespace
from .scheduling_async import SchedulingAsyncNamespace
from .schools import SchoolsNamespace
from .schools_async import SchoolsAsyncNamespace
from .staff import StaffNamespace
from .staff_async import StaffAsyncNamespace
from .students import StudentsNamespace
from .students_async import StudentsAsyncNamespace
from .system import SystemNamespace
from .system_async import SystemAsyncNamespace

NAMESPACE_REGISTRY = {
    "attendance": AttendanceNamespace,
    "gradebook": GradebookNamespace,
    "grades": GradesNamespace,
    "pre_enrollment": PreEnrollmentNamespace,
    "scheduling": SchedulingNamespace,
    "schools": SchoolsNamespace,
    "staff": StaffNamespace,
    "students": StudentsNamespace,
    "system": SystemNamespace,
}

ASYNC_NAMESPACE_REGISTRY = {
    "attendance": AttendanceAsyncNamespace,
    "gradebook": GradebookAsyncNamespace,
    "grades": GradesAsyncNamespace,
    "pre_enrollment": PreEnrollmentAsyncNamespace,
    "scheduling": SchedulingAsyncNamespace,
    "schools": SchoolsAsyncNamespace,
    "staff": StaffAsyncNamespace,
    "students": StudentsAsyncNamespace,
    "system": SystemAsyncNamespace,
}

OPERATION_INVENTORY = {
    "system.get_aeries_installation_information": "/api/v5/systeminfo",
    "schools.get_school_information": "/api/v5/schools/{SchoolCode}",
    "schools.get_school_terms": "/api/v5/schools/{SchoolCode}/terms",
    "schools.get_school_calendar": "/api/v5/schools/{SchoolCode}/calendar",
    "schools.get_bell_schedule": "/api/v5/schools/{SchoolCode}/BellSchedule",
    "schools.get_bell_schedule_date_date": "/api/v5/schools/{SchoolCode}/BellSchedule/date/{Date}",
    "schools.get_absence_codes": "/api/v5/schools/{SchoolCode}/AbsenceCodes/{AbsenceCode}",
    "schools.get_code_sets": "/api/v5/codes/{Table}/{Field}",
    "pre_enrollment.pre_enroll_student": "/api/v5/commands/preenrollstudent/{StudentID}",
    "pre_enrollment.pre_enroll_inactive_student": "/api/v5/PreEnrollInactiveStudent/{StudentID}/{NextSchoolCode}",
    "students.get_student_information": "/api/v5/schools/{SchoolCode}/students/{StudentID}",
    "students.get_student_information_grade_grade_level": "/api/v5/schools/{SchoolCode}/students/grade/{GradeLevel}",
    "students.get_student_information_sn_student_number": "/api/v5/schools/{SchoolCode}/students/sn/{StudentNumber}",
    "students.create_student_information_create": "/api/v5/schools/{SchoolCode}/InsertStudent",
    "students.create_student_information_update": "/api/v5/UpdateStudent/{StudentID}",
    "students.create_update_address": "/api/v5/UpdateStudentAddress/{StudentID}",
    "students.get_student_information_extended": "/api/v5/schools/{SchoolCode}/students/{StudentID}/extended",
    "students.get_student_information_extended_grade_grade_level_extended": "/api/v5/schools/{SchoolCode}/students/grade/{GradeLevel}/extended",
    "students.get_student_information_extended_sn_student_number_extended": "/api/v5/schools/{SchoolCode}/students/sn/{StudentNumber}/extended",
    "students.get_student_data_changes": "/api/v5/StudentDataChanges/{DataArea}/{year}/{month}/{day}/{hour}/{minute}",
    "students.get_contacts": "/api/v5/schools/{SchoolCode}/contacts/{StudentID}",
    "students.create_contacts_create": "/api/v5/InsertContact/{StudentID}",
    "students.get_programs": "/api/v5/schools/{SchoolCode}/students/{StudentID}/programs",
    "students.get_test_scores": "/api/v5/students/{StudentID}/tests",
    "students.get_update_test_scores": "/api/v5/testing/UpdateScores",
    "students.get_college_entrance_test_scores": "/api/v5/schools/{SchoolCode}/CollegeTestScores/{StudentID}",
    "students.get_assertive_discipline": "/api/v5/schools/{SchoolCode}/AssertiveDiscipline/{StudentID}",
    "students.get_discipline": "/api/v5/schools/{SchoolCode}/Discipline/{StudentID}",
    "students.get_district_supplemental_student_data": "/api/v5/schools/{SchoolCode}/DistrictSupplemental/{StudentID}",
    "students.get_school_supplemental_student_data": "/api/v5/schools/{SchoolCode}/SchoolSupplemental/{StudentID}",
    "students.get_fees_and_fines": "/api/v5/schools/{SchoolCode}/fees/{StudentID}",
    "students.get_student_picture": "/api/v5/schools/{SchoolCode}/StudentPictures/{StudentID}",
    "students.get_student_groups": "/api/v5/schools/{SchoolCode}/StudentGroups",
    "grades.get_student_gp_as": "/api/v5/schools/{SchoolCode}/gpas/{StudentID}",
    "grades.get_student_grades": "/api/v5/schools/{SchoolCode}/Grades",
    "grades.get_student_report_cards": "/api/v5/schools/{SchoolCode}/ReportCard/{StudentID}",
    "grades.get_school_report_card_marking_periods": "/api/v5/schools/{SchoolCode}/ReportCardMarkingPeriods",
    "grades.get_school_graduation_requirements": "/api/v5/schools/{SchoolCode}/GraduationRequirements",
    "grades.get_student_graduation_status_summary": "/api/v5/schools/{SchoolCode}/GraduationStatusSummary/{StudentID}",
    "grades.get_student_graduation_status_summary_grade_grade_level": "/api/v5/schools/{SchoolCode}/GraduationStatusSummary/grade/{GradeLevel}",
    "grades.get_student_transcripts": "/api/v5/schools/{SchoolCode}/Transcript/{StudentID}",
    "grades.get_valid_marks": "/api/v5/schools/{SchoolCode}/validmarks",
    "attendance.get_student_enrollment_history": "/api/v5/enrollment/{StudentID}",
    "attendance.get_student_enrollment_history_year_academic_year": "/api/v5/enrollment/{StudentID}/year/{AcademicYear}",
    "attendance.get_student_enrollment_history_schools_school_code_enrollment_student_id": "/api/v5/schools/{SchoolCode}/enrollment/{StudentID}",
    "attendance.get_student_enrollment_history_schools_school_code_enrollment_student_id_year_academic_year": "/api/v5/schools/{SchoolCode}/enrollment/{StudentID}/year/{AcademicYear}",
    "attendance.get_student_attendance": "/api/v5/schools/{SchoolCode}/attendance/{StudentID}",
    "attendance.get_attendance_history_summary": "/api/v5/schools/{SchoolCode}/AttendanceHistory/summary/{StudentID}",
    "attendance.get_attendance_history_summary_year_year": "/api/v5/schools/{SchoolCode}/AttendanceHistory/summary/year/{year}",
    "attendance.get_attendance_history_details": "/api/v5/schools/{SchoolCode}/AttendanceHistory/details/{StudentID}",
    "attendance.get_attendance_history_details_year_year": "/api/v5/schools/{SchoolCode}/AttendanceHistory/details/year/{year}",
    "attendance.get_attendance_history_attendance_codes": "/api/v5/schools/{SchoolCode}/AttendanceHistory/AbsenceCodes",
    "attendance.get_attendance_history_attendance_codes_year_year": "/api/v5/schools/{SchoolCode}/AttendanceHistory/AbsenceCodes/year/{year}",
    "staff.get_staff_information": "/api/v5/staff/{StaffID}",
    "staff.create_staff_information_create": "/api/v5/staff",
    "staff.update_staff_information_update": "/api/v5/staff/{StaffID}",
    "scheduling.get_course_information": "/api/v5/courses/{CourseID}",
    "scheduling.get_course_data_changes": "/api/v5/CourseDataChanges/{year}/{month}/{day}/{hour}/{minute}",
    "scheduling.get_sections_from_master_schedule": "/api/v5/schools/{SchoolCode}/sections/{SectionNumber}",
    "scheduling.get_section_data_changes_from_master_schedule": "/api/v5/SectionDataChanges/{year}/{month}/{day}/{hour}/{minute}",
    "scheduling.get_staff_classes_sections": "/api/v5/staff/{StaffID}/classes",
    "scheduling.get_section_class_roster": "/api/v5/schools/{SchoolCode}/sections/{SectionNumber}/students",
    "scheduling.get_section_class_roster_data_changes": "/api/v5/SectionRosterDataChanges/{year}/{month}/{day}/{hour}/{minute}",
    "scheduling.get_section_from_scheduling_master_schedule": "/api/v5/schools/{SchoolCode}/scheduling/sections/{SectionNumber}",
    "scheduling.create_section_from_scheduling_master_schedule": "/api/v5/schools/{SchoolCode}/scheduling/sections",
    "gradebook.get_gradebook_information": "/api/v5/staff/{StaffID}/gradebooks",
    "gradebook.get_gradebook_information_schools_school_code_sections_section_number_gradebooks": "/api/v5/schools/{SchoolCode}/sections/{SectionNumber}/gradebooks",
    "gradebook.get_gradebook_information_gradebooks_gradebook_number": "/api/v5/gradebooks/{GradebookNumber}",
    "gradebook.get_assignment_information": "/api/v5/gradebooks/{GradebookNumber}/assignments/{AssignmentNumber}",
    "gradebook.get_assignment_information_assignments_unique_id": "/api/v5/gradebooks/Assignments/{UniqueID}",
    "gradebook.update_updating_assignment_information": "/api/v5/gradebooks/{GradebookNumber}/assignments/{AssignmentNumber}",
    "gradebook.update_updating_assignment_information_assignments_unique_id": "/api/v5/gradebooks/Assignments/{UniqueID}",
    "gradebook.create_inserting_a_new_assignment": "/api/v5/gradebooks/{GradebookNumber}/Assignments",
    "gradebook.get_final_mark_ranges": "/api/v5/gradebooks/{GradebookNumber}/FinalMarks",
    "gradebook.get_gradebook_student_information": "/api/v5/gradebooks/{GradebookNumber}/{GradebookTerm}/students/{StudentID}",
    "gradebook.get_assignment_scores": "/api/v5/gradebooks/{GradebookNumber}/assignments/{AssignmentNumber}/scores/{StudentID}",
    "gradebook.get_assignment_scores_assignments_unique_id_scores_student_id": "/api/v5/gradebooks/assignments/{UniqueID}/scores/{StudentID}",
    "gradebook.create_updating_assignment_scores": "/api/v5/gradebooks/{GradebookNumber}/assignments/{AssignmentNumber}/Scores",
    "gradebook.create_updating_assignment_scores_assignments_unique_id_scores": "/api/v5/gradebooks/assignments/{UniqueID}/Scores",
}
