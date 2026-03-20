"""Generated file.

This file was created by `tools/generate_sdk.py` from the committed Aeries
contract snapshot. Do not edit it by hand because the next generation run will
replace it.
"""

from __future__ import annotations


from pydantic import Field

from ..models import AeriesModel

class SchoolsGetAeriesInstallationInformationResponse(AeriesModel):
    """Response model for `system.get_aeries_installation_information`."""
    aeries_version: int | str | None = Field(default=None, alias="AeriesVersion", description="Current Aeries Version Number")
    database_year: str | None = Field(default=None, alias="DatabaseYear", description="The 9-character year based on the current database connection for the API. By default, this is the default year of the default database group. If a valid DatabaseYear was passed in the query string of the API request, then that will be reflected in this property")
    available_database_years: str | None = Field(default=None, alias="AvailableDatabaseYears", description="A list of available years. This comes from the Year elements under the default database group in the AeriesNetConnections config.")
    local_time_zone_name: str | None = Field(default=None, alias="LocalTimeZoneName", description="From the hosting server")
    current_date_time: str | None = Field(default=None, alias="CurrentDateTime", description="From the hosting server")

class SchoolsGetSchoolInformationResponse(AeriesModel):
    """Response model for `schools.get_school_information`."""
    address: str | None = Field(default=None, alias="Address", description="Street address")
    address_city: str | None = Field(default=None, alias="AddressCity", description="City")
    address_state: str | None = Field(default=None, alias="AddressState", description="State")
    address_zip_code: int | str | None = Field(default=None, alias="AddressZipCode", description="Zip code")
    address_zip_ext: int | str | None = Field(default=None, alias="AddressZipExt", description="Zip code extension")
    attendance_period: str | None = Field(default=None, alias="AttendancePeriod", description="The homeroom period for the school. This is used to determine the student’s homeroom teacher where applicable.")
    attendance_reporting: str | None = Field(default=None, alias="AttendanceReporting", description="Indicates whether the school uses Negative or Positive attendance reporting")
    attendance_type: str | None = Field(default=None, alias="AttendanceType", description="Indicates whether the school takes Daily or Period attendance")
    do_not_report: int | str | None = Field(default=None, alias="DoNotReport", description="Flag indicating that information from this school code is not to be included in federal/state reporting (e.g., CALPADS)")
    high_grade_level: str | None = Field(default=None, alias="HighGradeLevel", description="The highest academic grade level offered at this school")
    inactive_status_code: int | str | None = Field(default=None, alias="InactiveStatusCode", description="If anything other than a blank value, this school code is inactive in Aeries")
    low_grade_level: str | None = Field(default=None, alias="LowGradeLevel", description="The lowest academic grade level offered at this school")
    name: str | None = Field(default=None, alias="Name", description="The name of the school")
    phone_number: int | str | None = Field(default=None, alias="PhoneNumber", description="The phone number for the school, including area code (digits only)")
    principal_email_address: str | None = Field(default=None, alias="PrincipalEmailAddress", description="The email address of the school principal")
    principal_name: str | None = Field(default=None, alias="PrincipalName", description="The name of the school principal")
    schedule_basis: str | None = Field(default=None, alias="ScheduleBasis", description="Indicates whether the school schedule is based on Semester or Trimester")
    schedule_type: str | None = Field(default=None, alias="ScheduleType", description="Indicates the schedule type of the school. Return value will be Elementary, ElementaryAndMasterSchedule, MasterSchedule or Flex")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The numeric Aeries school code")
    session_type: int | str | None = Field(default=None, alias="SessionType", description="Indicates whether the school code represents a Regular, Summer, or Intersession school")
    state_county_id: int | str | None = Field(default=None, alias="StateCountyID", description="The 2-digit county part of the school’s county-district-school (CDS) code")
    state_district_id: int | str | None = Field(default=None, alias="StateDistrictID", description="The 5-digit district part of the school’s CDS code")
    state_school_id: int | str | None = Field(default=None, alias="StateSchoolID", description="The 7-digit school part of the CDS code")
    tracks: int | str | None = Field(default=None, alias="Tracks", description="The number of different attendance tracks used by the school")
    region_code: int | str | None = Field(default=None, alias="RegionCode", description="Region Code")
    state_charter_number: int | str | None = Field(default=None, alias="StateCharterNumber", description="State Charter Number")
    charter_status_code: int | str | None = Field(default=None, alias="CharterStatusCode", description="Charter Status")
    federal_tax_id: str | None = Field(default=None, alias="FederalTaxID", description="Federal Tax ID")
    federal_information_processing_standards_code: int | str | None = Field(default=None, alias="FederalInformationProcessingStandardsCode", description="Federal Information Processing Standards")
    quality_rating_and_improvement_system_participation_code: int | str | None = Field(default=None, alias="QualityRatingAndImprovementSystemParticipationCode", description="Quality Rating And Improvement System Participation Code")
    accreditation_status_code: int | str | None = Field(default=None, alias="AccreditationStatusCode", description="Accreditation Status")
    school_website: str | None = Field(default=None, alias="School Website", description="School Website")
    organization_category_code: int | str | None = Field(default=None, alias="OrganizationCategoryCode", description="Organization Category")
    school_category_code: int | str | None = Field(default=None, alias="SchoolCategoryCode", description="School Category")
    local_education_agency_type_code: int | str | None = Field(default=None, alias="LocalEducationAgencyTypeCode", description="Local Education Agency Type")
    title_i_part_a_code: int | str | None = Field(default=None, alias="TitleIPartACode", description="Title I Part A")
    nslp_status_code: int | str | None = Field(default=None, alias="NSLPStatusCode", description="NSLP Status")
    nces_school_iid: str | None = Field(default=None, alias="NCESSchoolIID", description="NCES School IID")

class SchoolsGetSchoolTermsResponse(AeriesModel):
    """Response model for `schools.get_school_terms`."""
    end_date: str | None = Field(default=None, alias="EndDate", description="End date of the term")
    start_date: str | None = Field(default=None, alias="StartDate", description="Start date of the term")
    term_code: int | str | None = Field(default=None, alias="TermCode", description="Code value of the term")
    term_description: str | None = Field(default=None, alias="TermDescription", description="Description of the term")
    first_half_end_date: str | None = Field(default=None, alias="FirstHalfEndDate", description="First Half End Date for Hexamesters")
    second_half_start_date: str | None = Field(default=None, alias="SecondHalfStartDate", description="Second Half Start Date for Hexamesters")
    track_terms: str | None = Field(default=None, alias="TrackTerms", description="The Term which applies to the Track Calendar")

class SchoolsGetSchoolCalendarResponse(AeriesModel):
    """Response model for `schools.get_school_calendar`."""
    ab_day: str | None = Field(default=None, alias="ABDay", description="Whether this school day is an “A” day or “B” day if applicable")
    attendance_month: int | str | None = Field(default=None, alias="AttendanceMonth", description="The attendance month number for this calendar day. In Aeries, an attendance month represents 4 weeks of Mondays-Fridays, for 20 total days")
    attendance_month_locked: int | str | None = Field(default=None, alias="AttendanceMonthLocked", description="Flag indicating whether this attendance month is locked for editing. Districts typically lock an attendance month after reconciling the apportionment data for that month for fiscal accountability purposes.")
    calendar_date: str | None = Field(default=None, alias="CalendarDate", description="The date for this calendar day number")
    calendar_day_number: int | str | None = Field(default=None, alias="CalendarDayNumber", description="The calendar day number. This is normally a value between 1 and 200")
    holiday_code: int | str | None = Field(default=None, alias="HolidayCode", description="A code representing a special status for this day such as minimum day, school holiday, staff development day, etc. These values are hard-coded. @ = School not in session % = Minimum Day # = School Holiday + = Parent Conference $ = Staff Development")
    period_block_pattern: str | None = Field(default=None, alias="PeriodBlockPattern", description="A string indicating which class periods meet on this day. For each digit 0-9 that is present in this string, that class period meets on this day.")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    total_apportionment: str | None = Field(default=None, alias="TotalApportionment", description="The total apportioned attendance for this day")
    total_enrollment: str | None = Field(default=None, alias="TotalEnrollment", description="The total student enrollment for this day")
    track_holiday_holiday_code: int | str | None = Field(default=None, alias="TrackHoliday.HolidayCode", description="Similar to HolidayCode, but for a specific track")
    track_holiday_track_code: int | str | None = Field(default=None, alias="TrackHoliday.TrackCode", description="The track code, a letter from A-Z")
    track_holiday_track_number: int | str | None = Field(default=None, alias="TrackHoliday.TrackNumber", description="The track number, a number from 1-26")

class SchoolsGetBellScheduleResponse(AeriesModel):
    """Response model for `schools.get_bell_schedule`."""
    calendar_day_number: int | str | None = Field(default=None, alias="CalendarDayNumber", description="The day number from the school’s calendar")
    end_time: str | None = Field(default=None, alias="EndTime", description="The time this class period ends according to the bell schedule. Value is a datetime format, but only the time part is relevant.")
    period: str | None = Field(default=None, alias="Period", description="The class period (0-9)")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    start_time: str | None = Field(default=None, alias="StartTime", description="The time this class period starts according to the bell schedule. Value is a datetime format, but only the time part is relevant.")

class SchoolsGetBellScheduleDateDateResponse(AeriesModel):
    """Response model for `schools.get_bell_schedule_date_date`."""
    calendar_day_number: int | str | None = Field(default=None, alias="CalendarDayNumber", description="The day number from the school’s calendar")
    end_time: str | None = Field(default=None, alias="EndTime", description="The time this class period ends according to the bell schedule. Value is a datetime format, but only the time part is relevant.")
    period: str | None = Field(default=None, alias="Period", description="The class period (0-9)")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    start_time: str | None = Field(default=None, alias="StartTime", description="The time this class period starts according to the bell schedule. Value is a datetime format, but only the time part is relevant.")

class SchoolsGetAbsenceCodesResponse(AeriesModel):
    """Response model for `schools.get_absence_codes`."""
    abbreviation: int | str | None = Field(default=None, alias="Abbreviation", description="The abbreviated name (max 3 characters) for this absence code")
    absence_code: int | str | None = Field(default=None, alias="AbsenceCode", description="The absence code (1 character). This will typically be a letter A-Z but may be a digit.")
    count_on_report_card: int | str | None = Field(default=None, alias="CountOnReportCard", description="Indicates whether this absence code counts toward attendance totals on the grade report card.")
    counts_for_ada: int | str | None = Field(default=None, alias="CountsForADA", description="Indicates whether this absence code counts toward the school’s ADA apportionment calculation.")
    include_in_parent_notifications: int | str | None = Field(default=None, alias="IncludeInParentNotifications", description="Indicates whether this absence code should be included when notifications are sent to parents (e.g., automated attendance calls).")
    include_on_letters: int | str | None = Field(default=None, alias="IncludeOnLetters", description="Indicates whether this absence code should be included on letters sent to parents")
    include_on_reports: int | str | None = Field(default=None, alias="IncludeOnReports", description="Indicates whether this absence code should print on attendance reports.")
    is_partial_day_truant: int | str | None = Field(default=None, alias="IsPartialDayTruant", description="Indicates whether this absence code represents a partial day truancy. It would normally be used for a student who is more than 30 minutes late for class.")
    is_suspension: int | str | None = Field(default=None, alias="IsSuspension", description="Indicates whether this absence code represents a suspension (may be in-school or out-of-school).")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    title: int | str | None = Field(default=None, alias="Title", description="The full name (max 10 characters) for this absence code")
    type_code: int | str | None = Field(default=None, alias="TypeCode", description="A code representing the type of absence code.")
    type_description: int | str | None = Field(default=None, alias="TypeDescription", description="The description corresponding to the TypeCode. 1 = Unverified Absence 2 = Excused Absence 3 = Unexcused Absence 4 = Verified Not Absent 5 = Tardy 6 = Present 7 (not currently used) 8 = Verified Excused Tardy 9 = Verified Unexcused Tardy")
    is_temporarily_not_enrolled: str | None = Field(default=None, alias="IsTemporarilyNotEnrolled", description="Indicates whether the Student was Temporarily Not Enrolled")
    independent_study_code: int | str | None = Field(default=None, alias="IndependentStudyCode", description="Used to Indicate a Students completion/incompletion of Independent Study Work")
    color_code: int | str | None = Field(default=None, alias="ColorCode", description="If the School uses it, the color code assigned to the Absence Code.")

class SchoolsGetCodeSetsResponse(AeriesModel):
    """Response model for `schools.get_code_sets`."""
    aeries_code: int | str | None = Field(default=None, alias="AeriesCode", description="Identifies the internal Aeries code corresponding to the code value. Currently this is only used to match coded Grade Level values to the numeric grade levels that Aeries uses internally. For example, Kindergarten is coded as “K” but internally stored as 0.")
    category: int | str | None = Field(default=None, alias="Category", description="The category for this code. In some areas of the system, Aeries supports grouping related codes by categories.")
    code: int | str | None = Field(default=None, alias="Code", description="The code value")
    correspondence_language_code1: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode1", description="The first language code for which a translated description is available")
    correspondence_language_code2: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode2", description="The second language code for which a translated description is available")
    correspondence_language_code3: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode3", description="The third language code for which a translated description is available")
    correspondence_language_code4: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode4", description="The fourth language code for which a translated description is available")
    correspondence_language_code5: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode5", description="The fifth language code for which a translated description is available")
    correspondence_language_code6: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode6", description="The sixth language code for which a translated description is available")
    description: int | str | None = Field(default=None, alias="Description", description="The description for the code in English")
    description_for_language1: int | str | None = Field(default=None, alias="DescriptionForLanguage1", description="The first translated description of the code")
    description_for_language2: int | str | None = Field(default=None, alias="DescriptionForLanguage2", description="The second translated description of the code")
    description_for_language3: int | str | None = Field(default=None, alias="DescriptionForLanguage3", description="The third translated description of the code")
    description_for_language4: int | str | None = Field(default=None, alias="DescriptionForLanguage4", description="The fourth translated description of the code")
    description_for_language5: int | str | None = Field(default=None, alias="DescriptionForLanguage5", description="The fifth translated description of the code")
    description_for_language6: int | str | None = Field(default=None, alias="DescriptionForLanguage6", description="The sixth translated description of the code")
    field: int | str | None = Field(default=None, alias="Field", description="The Aeries field to which this code belongs")
    numeric_value: int | str | None = Field(default=None, alias="NumericValue", description="Only used for certain table/field codes. The meaning depends on the table/field. Ex: for Fees/FeeCode, the NumericValue is the default amount of the fee.")
    sort_order: int | str | None = Field(default=None, alias="SortOrder", description="The sort order for this code. In Aeries drop-down lists, codes are sorted alphabetically unless a sort order greater than zero is specified")
    status: int | str | None = Field(default=None, alias="Status", description="Any value other than a blank means this code is inactive. It may still be found on existing records, but users are not able to select this code for new records.")
    table: int | str | None = Field(default=None, alias="Table", description="The Aeries table to which this code belongs")

class PreEnrollmentPreEnrollStudentResponse(AeriesModel):
    """Response model for `pre_enrollment.pre_enroll_student`."""
    pass

class PreEnrollmentPreEnrollInactiveStudentResponse(AeriesModel):
    """Response model for `pre_enrollment.pre_enroll_inactive_student`."""
    pass

class StudentsGetStudentInformationResponse(AeriesModel):
    """Response model for `students.get_student_information`."""
    address_verified: str | None = Field(default=None, alias="AddressVerified", description="Indicates whether the student’s residence address has been verified")
    attendance_program_code_additional1: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional1", description="An additional specialized attendance program to which this student belongs")
    attendance_program_code_additional2: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional2", description="An additional specialized attendance program to which this student belongs")
    attendance_program_code_primary: int | str | None = Field(default=None, alias="AttendanceProgramCodePrimary", description="The primary specialized attendance program to which this student currently belongs. Attendance programs are used to separate certain students’ attendance data in the monthly apportionment (ADA) calculations.")
    birthdate: str | None = Field(default=None, alias="Birthdate", description="Date of Birth")
    correspondence_language_code: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode", description="The preferred language for correspondence sent regarding this student")
    counselor_number: int | str | None = Field(default=None, alias="CounselorNumber", description="If the school is using Staff ID Based Counselors, then the CounselorNumber property is simply mapped to STU.CNS. If the school is NOT using Staff ID Based Counselors, then we will look up the TCH record for STU.CU and map CounselorNumber to TCH.ID.")
    student_personal_email_address: str | None = Field(default=None, alias="StudentPersonalEmailAddress", description="Student's Personal EmailAddress")
    district_enter_date: str | None = Field(default=None, alias="DistrictEnterDate", description="Date student entered the district")
    early_warning_points: int | str | None = Field(default=None, alias="EarlyWarningPoints", description="The total number of “early warning” points. Used by the Aeries Analytics Early Warning System")
    ethnicity_code: int | str | None = Field(default=None, alias="EthnicityCode", description="“Y” or “N” Hispanic indicator")
    family_key: str | None = Field(default=None, alias="FamilyKey", description="Numeric. Students with the same nonzero Family Key are considered “siblings” in Aeries.")
    first_name: str | None = Field(default=None, alias="FirstName", description="Student’s legal first name")
    first_name_alias: str | None = Field(default=None, alias="FirstNameAlias", description="Student’s first name alias")
    grade: str | None = Field(default=None, alias="Grade", description="0-18 Student’s grade level")
    high_scheduling_period: str | None = Field(default=None, alias="HighSchedulingPeriod", description="0-9 Highest scheduling period")
    home_language_code: int | str | None = Field(default=None, alias="HomeLanguageCode", description="The student’s primary language for purposes of English Learner classification")
    home_phone: int | str | None = Field(default=None, alias="HomePhone", description="Student’s home phone number")
    home_room_teacher_number: int | str | None = Field(default=None, alias="HomeRoomTeacherNumber", description="A school-based Aeries teacher number. The student’s homeroom teacher based on the class period the school designates as homeroom in daily attendance schools (elementary and secondary)")
    inactive_status_code: int | str | None = Field(default=None, alias="InactiveStatusCode", description="Student’s status (blank is active)")
    language_fluency_code: int | str | None = Field(default=None, alias="LanguageFluencyCode", description="Language fluency code")
    last_name: str | None = Field(default=None, alias="LastName", description="Student’s legal last name")
    last_name_alias: str | None = Field(default=None, alias="LastNameAlias", description="Student’s last name alias")
    locker_number: int | str | None = Field(default=None, alias="LockerNumber", description="Locker number")
    low_scheduling_period: str | None = Field(default=None, alias="LowSchedulingPeriod", description="0-9 Lowest scheduling period")
    mailing_address: str | None = Field(default=None, alias="MailingAddress", description="Student’s mailing address")
    mailing_address_city: str | None = Field(default=None, alias="MailingAddressCity", description="Student’s mailing address city")
    mailing_address_state: str | None = Field(default=None, alias="MailingAddressState", description="Student’s mailing address state")
    mailing_address_zip_code: int | str | None = Field(default=None, alias="MailingAddressZipCode", description="Student’s mailing address zip code")
    mailing_address_zip_ext: int | str | None = Field(default=None, alias="MailingAddressZipExt", description="Student’s mailing address zip code extension")
    middle_name: str | None = Field(default=None, alias="MiddleName", description="Student’s legal middle name")
    middle_name_alias: str | None = Field(default=None, alias="MiddleNameAlias", description="Student’s middle name alias")
    network_login_id: str | None = Field(default=None, alias="NetworkLoginID", description="Student’s Network Login ID. Districts may use this for various purposes, but most commonly for a directory services (e.g., Active Directory) username")
    notification_preference_code: int | str | None = Field(default=None, alias="NotificationPreferenceCode", description="Indicates the Aeries Communications notification preference of this student")
    old_student_id: str | None = Field(default=None, alias="OldStudentID", description="Student's Old permanent ID")
    parent_ed_level_code: int | str | None = Field(default=None, alias="ParentEdLevelCode", description="Highest level of education completed by either of the student’s parents (for socioeconomically disadvantaged classification purposes)")
    parent_email_address: str | None = Field(default=None, alias="ParentEmailAddress", description="(deprecated, but still in use by some customers) The primary parent/guardian email address")
    parent_guardian_name: str | None = Field(default=None, alias="ParentGuardianName", description="Parent/Guardian name")
    student_id: str | None = Field(default=None, alias="StudentID", description="Student ID")
    race_code1: int | str | None = Field(default=None, alias="RaceCode1", description="Student’s first reported race")
    race_code2: int | str | None = Field(default=None, alias="RaceCode2", description="Student’s second reported race")
    race_code3: int | str | None = Field(default=None, alias="RaceCode3", description="Student’s third reported race")
    race_code4: int | str | None = Field(default=None, alias="RaceCode4", description="Student’s fourth reported race")
    race_code5: int | str | None = Field(default=None, alias="RaceCode5", description="Student’s fifth reported race")
    residence_address: str | None = Field(default=None, alias="ResidenceAddress", description="Residence address")
    residence_address_city: str | None = Field(default=None, alias="ResidenceAddressCity", description="Residence address city")
    residence_address_state: str | None = Field(default=None, alias="ResidenceAddressState", description="Residence address state")
    residence_address_zip_code: int | str | None = Field(default=None, alias="ResidenceAddressZipCode", description="Residence address zip code")
    residence_address_zip_ext: int | str | None = Field(default=None, alias="ResidenceAddressZipExt", description="Residence address zip code extension")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="Aeries school code")
    school_enter_date: str | None = Field(default=None, alias="SchoolEnterDate", description="Date student first entered this school")
    school_leave_date: str | None = Field(default=None, alias="SchoolLeaveDate", description="Date student left this school")
    gender: int | str | None = Field(default=None, alias="Gender", description="Student'sg ender (May be M or F or another coded value for non-binary gender identifications)")
    state_student_id: str | None = Field(default=None, alias="StateStudentID", description="Statewide Student ID")
    student_email_address: str | None = Field(default=None, alias="StudentEmailAddress", description="Student’s email address")
    student_mobile_phone: int | str | None = Field(default=None, alias="StudentMobilePhone", description="Mobile phone number")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="School-based Student Number")
    track: str | None = Field(default=None, alias="Track", description="Student’s attendance track")
    user_code1: int | str | None = Field(default=None, alias="UserCode1", description="User-defined code 1")
    user_code10: int | str | None = Field(default=None, alias="UserCode10", description="User-defined code 10")
    user_code11: int | str | None = Field(default=None, alias="UserCode11", description="User-defined code 11")
    user_code12: int | str | None = Field(default=None, alias="UserCode12", description="User-defined code 12")
    user_code13: int | str | None = Field(default=None, alias="UserCode13", description="User-defined code 13")
    user_code2: int | str | None = Field(default=None, alias="UserCode2", description="User-defined code 2")
    user_code3: int | str | None = Field(default=None, alias="UserCode3", description="User-defined code 3")
    user_code4: int | str | None = Field(default=None, alias="UserCode4", description="User-defined code 4")
    user_code5: int | str | None = Field(default=None, alias="UserCode5", description="User-defined code 5")
    user_code6: int | str | None = Field(default=None, alias="UserCode6", description="User-defined code 6")
    user_code7: int | str | None = Field(default=None, alias="UserCode7", description="User-defined code 7")
    user_code8: int | str | None = Field(default=None, alias="UserCode8", description="User-defined code 8")
    user_code9: int | str | None = Field(default=None, alias="UserCode9", description="User-defined code 9")

class StudentsGetStudentInformationGradeGradeLevelResponse(AeriesModel):
    """Response model for `students.get_student_information_grade_grade_level`."""
    address_verified: str | None = Field(default=None, alias="AddressVerified", description="Indicates whether the student’s residence address has been verified")
    attendance_program_code_additional1: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional1", description="An additional specialized attendance program to which this student belongs")
    attendance_program_code_additional2: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional2", description="An additional specialized attendance program to which this student belongs")
    attendance_program_code_primary: int | str | None = Field(default=None, alias="AttendanceProgramCodePrimary", description="The primary specialized attendance program to which this student currently belongs. Attendance programs are used to separate certain students’ attendance data in the monthly apportionment (ADA) calculations.")
    birthdate: str | None = Field(default=None, alias="Birthdate", description="Date of Birth")
    correspondence_language_code: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode", description="The preferred language for correspondence sent regarding this student")
    counselor_number: int | str | None = Field(default=None, alias="CounselorNumber", description="If the school is using Staff ID Based Counselors, then the CounselorNumber property is simply mapped to STU.CNS. If the school is NOT using Staff ID Based Counselors, then we will look up the TCH record for STU.CU and map CounselorNumber to TCH.ID.")
    student_personal_email_address: str | None = Field(default=None, alias="StudentPersonalEmailAddress", description="Student's Personal EmailAddress")
    district_enter_date: str | None = Field(default=None, alias="DistrictEnterDate", description="Date student entered the district")
    early_warning_points: int | str | None = Field(default=None, alias="EarlyWarningPoints", description="The total number of “early warning” points. Used by the Aeries Analytics Early Warning System")
    ethnicity_code: int | str | None = Field(default=None, alias="EthnicityCode", description="“Y” or “N” Hispanic indicator")
    family_key: str | None = Field(default=None, alias="FamilyKey", description="Numeric. Students with the same nonzero Family Key are considered “siblings” in Aeries.")
    first_name: str | None = Field(default=None, alias="FirstName", description="Student’s legal first name")
    first_name_alias: str | None = Field(default=None, alias="FirstNameAlias", description="Student’s first name alias")
    grade: str | None = Field(default=None, alias="Grade", description="0-18 Student’s grade level")
    high_scheduling_period: str | None = Field(default=None, alias="HighSchedulingPeriod", description="0-9 Highest scheduling period")
    home_language_code: int | str | None = Field(default=None, alias="HomeLanguageCode", description="The student’s primary language for purposes of English Learner classification")
    home_phone: int | str | None = Field(default=None, alias="HomePhone", description="Student’s home phone number")
    home_room_teacher_number: int | str | None = Field(default=None, alias="HomeRoomTeacherNumber", description="A school-based Aeries teacher number. The student’s homeroom teacher based on the class period the school designates as homeroom in daily attendance schools (elementary and secondary)")
    inactive_status_code: int | str | None = Field(default=None, alias="InactiveStatusCode", description="Student’s status (blank is active)")
    language_fluency_code: int | str | None = Field(default=None, alias="LanguageFluencyCode", description="Language fluency code")
    last_name: str | None = Field(default=None, alias="LastName", description="Student’s legal last name")
    last_name_alias: str | None = Field(default=None, alias="LastNameAlias", description="Student’s last name alias")
    locker_number: int | str | None = Field(default=None, alias="LockerNumber", description="Locker number")
    low_scheduling_period: str | None = Field(default=None, alias="LowSchedulingPeriod", description="0-9 Lowest scheduling period")
    mailing_address: str | None = Field(default=None, alias="MailingAddress", description="Student’s mailing address")
    mailing_address_city: str | None = Field(default=None, alias="MailingAddressCity", description="Student’s mailing address city")
    mailing_address_state: str | None = Field(default=None, alias="MailingAddressState", description="Student’s mailing address state")
    mailing_address_zip_code: int | str | None = Field(default=None, alias="MailingAddressZipCode", description="Student’s mailing address zip code")
    mailing_address_zip_ext: int | str | None = Field(default=None, alias="MailingAddressZipExt", description="Student’s mailing address zip code extension")
    middle_name: str | None = Field(default=None, alias="MiddleName", description="Student’s legal middle name")
    middle_name_alias: str | None = Field(default=None, alias="MiddleNameAlias", description="Student’s middle name alias")
    network_login_id: str | None = Field(default=None, alias="NetworkLoginID", description="Student’s Network Login ID. Districts may use this for various purposes, but most commonly for a directory services (e.g., Active Directory) username")
    notification_preference_code: int | str | None = Field(default=None, alias="NotificationPreferenceCode", description="Indicates the Aeries Communications notification preference of this student")
    old_student_id: str | None = Field(default=None, alias="OldStudentID", description="Student's Old permanent ID")
    parent_ed_level_code: int | str | None = Field(default=None, alias="ParentEdLevelCode", description="Highest level of education completed by either of the student’s parents (for socioeconomically disadvantaged classification purposes)")
    parent_email_address: str | None = Field(default=None, alias="ParentEmailAddress", description="(deprecated, but still in use by some customers) The primary parent/guardian email address")
    parent_guardian_name: str | None = Field(default=None, alias="ParentGuardianName", description="Parent/Guardian name")
    student_id: str | None = Field(default=None, alias="StudentID", description="Student ID")
    race_code1: int | str | None = Field(default=None, alias="RaceCode1", description="Student’s first reported race")
    race_code2: int | str | None = Field(default=None, alias="RaceCode2", description="Student’s second reported race")
    race_code3: int | str | None = Field(default=None, alias="RaceCode3", description="Student’s third reported race")
    race_code4: int | str | None = Field(default=None, alias="RaceCode4", description="Student’s fourth reported race")
    race_code5: int | str | None = Field(default=None, alias="RaceCode5", description="Student’s fifth reported race")
    residence_address: str | None = Field(default=None, alias="ResidenceAddress", description="Residence address")
    residence_address_city: str | None = Field(default=None, alias="ResidenceAddressCity", description="Residence address city")
    residence_address_state: str | None = Field(default=None, alias="ResidenceAddressState", description="Residence address state")
    residence_address_zip_code: int | str | None = Field(default=None, alias="ResidenceAddressZipCode", description="Residence address zip code")
    residence_address_zip_ext: int | str | None = Field(default=None, alias="ResidenceAddressZipExt", description="Residence address zip code extension")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="Aeries school code")
    school_enter_date: str | None = Field(default=None, alias="SchoolEnterDate", description="Date student first entered this school")
    school_leave_date: str | None = Field(default=None, alias="SchoolLeaveDate", description="Date student left this school")
    gender: int | str | None = Field(default=None, alias="Gender", description="Student'sg ender (May be M or F or another coded value for non-binary gender identifications)")
    state_student_id: str | None = Field(default=None, alias="StateStudentID", description="Statewide Student ID")
    student_email_address: str | None = Field(default=None, alias="StudentEmailAddress", description="Student’s email address")
    student_mobile_phone: int | str | None = Field(default=None, alias="StudentMobilePhone", description="Mobile phone number")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="School-based Student Number")
    track: str | None = Field(default=None, alias="Track", description="Student’s attendance track")
    user_code1: int | str | None = Field(default=None, alias="UserCode1", description="User-defined code 1")
    user_code10: int | str | None = Field(default=None, alias="UserCode10", description="User-defined code 10")
    user_code11: int | str | None = Field(default=None, alias="UserCode11", description="User-defined code 11")
    user_code12: int | str | None = Field(default=None, alias="UserCode12", description="User-defined code 12")
    user_code13: int | str | None = Field(default=None, alias="UserCode13", description="User-defined code 13")
    user_code2: int | str | None = Field(default=None, alias="UserCode2", description="User-defined code 2")
    user_code3: int | str | None = Field(default=None, alias="UserCode3", description="User-defined code 3")
    user_code4: int | str | None = Field(default=None, alias="UserCode4", description="User-defined code 4")
    user_code5: int | str | None = Field(default=None, alias="UserCode5", description="User-defined code 5")
    user_code6: int | str | None = Field(default=None, alias="UserCode6", description="User-defined code 6")
    user_code7: int | str | None = Field(default=None, alias="UserCode7", description="User-defined code 7")
    user_code8: int | str | None = Field(default=None, alias="UserCode8", description="User-defined code 8")
    user_code9: int | str | None = Field(default=None, alias="UserCode9", description="User-defined code 9")

class StudentsGetStudentInformationSnStudentNumberResponse(AeriesModel):
    """Response model for `students.get_student_information_sn_student_number`."""
    address_verified: str | None = Field(default=None, alias="AddressVerified", description="Indicates whether the student’s residence address has been verified")
    attendance_program_code_additional1: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional1", description="An additional specialized attendance program to which this student belongs")
    attendance_program_code_additional2: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional2", description="An additional specialized attendance program to which this student belongs")
    attendance_program_code_primary: int | str | None = Field(default=None, alias="AttendanceProgramCodePrimary", description="The primary specialized attendance program to which this student currently belongs. Attendance programs are used to separate certain students’ attendance data in the monthly apportionment (ADA) calculations.")
    birthdate: str | None = Field(default=None, alias="Birthdate", description="Date of Birth")
    correspondence_language_code: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode", description="The preferred language for correspondence sent regarding this student")
    counselor_number: int | str | None = Field(default=None, alias="CounselorNumber", description="If the school is using Staff ID Based Counselors, then the CounselorNumber property is simply mapped to STU.CNS. If the school is NOT using Staff ID Based Counselors, then we will look up the TCH record for STU.CU and map CounselorNumber to TCH.ID.")
    student_personal_email_address: str | None = Field(default=None, alias="StudentPersonalEmailAddress", description="Student's Personal EmailAddress")
    district_enter_date: str | None = Field(default=None, alias="DistrictEnterDate", description="Date student entered the district")
    early_warning_points: int | str | None = Field(default=None, alias="EarlyWarningPoints", description="The total number of “early warning” points. Used by the Aeries Analytics Early Warning System")
    ethnicity_code: int | str | None = Field(default=None, alias="EthnicityCode", description="“Y” or “N” Hispanic indicator")
    family_key: str | None = Field(default=None, alias="FamilyKey", description="Numeric. Students with the same nonzero Family Key are considered “siblings” in Aeries.")
    first_name: str | None = Field(default=None, alias="FirstName", description="Student’s legal first name")
    first_name_alias: str | None = Field(default=None, alias="FirstNameAlias", description="Student’s first name alias")
    grade: str | None = Field(default=None, alias="Grade", description="0-18 Student’s grade level")
    high_scheduling_period: str | None = Field(default=None, alias="HighSchedulingPeriod", description="0-9 Highest scheduling period")
    home_language_code: int | str | None = Field(default=None, alias="HomeLanguageCode", description="The student’s primary language for purposes of English Learner classification")
    home_phone: int | str | None = Field(default=None, alias="HomePhone", description="Student’s home phone number")
    home_room_teacher_number: int | str | None = Field(default=None, alias="HomeRoomTeacherNumber", description="A school-based Aeries teacher number. The student’s homeroom teacher based on the class period the school designates as homeroom in daily attendance schools (elementary and secondary)")
    inactive_status_code: int | str | None = Field(default=None, alias="InactiveStatusCode", description="Student’s status (blank is active)")
    language_fluency_code: int | str | None = Field(default=None, alias="LanguageFluencyCode", description="Language fluency code")
    last_name: str | None = Field(default=None, alias="LastName", description="Student’s legal last name")
    last_name_alias: str | None = Field(default=None, alias="LastNameAlias", description="Student’s last name alias")
    locker_number: int | str | None = Field(default=None, alias="LockerNumber", description="Locker number")
    low_scheduling_period: str | None = Field(default=None, alias="LowSchedulingPeriod", description="0-9 Lowest scheduling period")
    mailing_address: str | None = Field(default=None, alias="MailingAddress", description="Student’s mailing address")
    mailing_address_city: str | None = Field(default=None, alias="MailingAddressCity", description="Student’s mailing address city")
    mailing_address_state: str | None = Field(default=None, alias="MailingAddressState", description="Student’s mailing address state")
    mailing_address_zip_code: int | str | None = Field(default=None, alias="MailingAddressZipCode", description="Student’s mailing address zip code")
    mailing_address_zip_ext: int | str | None = Field(default=None, alias="MailingAddressZipExt", description="Student’s mailing address zip code extension")
    middle_name: str | None = Field(default=None, alias="MiddleName", description="Student’s legal middle name")
    middle_name_alias: str | None = Field(default=None, alias="MiddleNameAlias", description="Student’s middle name alias")
    network_login_id: str | None = Field(default=None, alias="NetworkLoginID", description="Student’s Network Login ID. Districts may use this for various purposes, but most commonly for a directory services (e.g., Active Directory) username")
    notification_preference_code: int | str | None = Field(default=None, alias="NotificationPreferenceCode", description="Indicates the Aeries Communications notification preference of this student")
    old_student_id: str | None = Field(default=None, alias="OldStudentID", description="Student's Old permanent ID")
    parent_ed_level_code: int | str | None = Field(default=None, alias="ParentEdLevelCode", description="Highest level of education completed by either of the student’s parents (for socioeconomically disadvantaged classification purposes)")
    parent_email_address: str | None = Field(default=None, alias="ParentEmailAddress", description="(deprecated, but still in use by some customers) The primary parent/guardian email address")
    parent_guardian_name: str | None = Field(default=None, alias="ParentGuardianName", description="Parent/Guardian name")
    student_id: str | None = Field(default=None, alias="StudentID", description="Student ID")
    race_code1: int | str | None = Field(default=None, alias="RaceCode1", description="Student’s first reported race")
    race_code2: int | str | None = Field(default=None, alias="RaceCode2", description="Student’s second reported race")
    race_code3: int | str | None = Field(default=None, alias="RaceCode3", description="Student’s third reported race")
    race_code4: int | str | None = Field(default=None, alias="RaceCode4", description="Student’s fourth reported race")
    race_code5: int | str | None = Field(default=None, alias="RaceCode5", description="Student’s fifth reported race")
    residence_address: str | None = Field(default=None, alias="ResidenceAddress", description="Residence address")
    residence_address_city: str | None = Field(default=None, alias="ResidenceAddressCity", description="Residence address city")
    residence_address_state: str | None = Field(default=None, alias="ResidenceAddressState", description="Residence address state")
    residence_address_zip_code: int | str | None = Field(default=None, alias="ResidenceAddressZipCode", description="Residence address zip code")
    residence_address_zip_ext: int | str | None = Field(default=None, alias="ResidenceAddressZipExt", description="Residence address zip code extension")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="Aeries school code")
    school_enter_date: str | None = Field(default=None, alias="SchoolEnterDate", description="Date student first entered this school")
    school_leave_date: str | None = Field(default=None, alias="SchoolLeaveDate", description="Date student left this school")
    gender: int | str | None = Field(default=None, alias="Gender", description="Student'sg ender (May be M or F or another coded value for non-binary gender identifications)")
    state_student_id: str | None = Field(default=None, alias="StateStudentID", description="Statewide Student ID")
    student_email_address: str | None = Field(default=None, alias="StudentEmailAddress", description="Student’s email address")
    student_mobile_phone: int | str | None = Field(default=None, alias="StudentMobilePhone", description="Mobile phone number")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="School-based Student Number")
    track: str | None = Field(default=None, alias="Track", description="Student’s attendance track")
    user_code1: int | str | None = Field(default=None, alias="UserCode1", description="User-defined code 1")
    user_code10: int | str | None = Field(default=None, alias="UserCode10", description="User-defined code 10")
    user_code11: int | str | None = Field(default=None, alias="UserCode11", description="User-defined code 11")
    user_code12: int | str | None = Field(default=None, alias="UserCode12", description="User-defined code 12")
    user_code13: int | str | None = Field(default=None, alias="UserCode13", description="User-defined code 13")
    user_code2: int | str | None = Field(default=None, alias="UserCode2", description="User-defined code 2")
    user_code3: int | str | None = Field(default=None, alias="UserCode3", description="User-defined code 3")
    user_code4: int | str | None = Field(default=None, alias="UserCode4", description="User-defined code 4")
    user_code5: int | str | None = Field(default=None, alias="UserCode5", description="User-defined code 5")
    user_code6: int | str | None = Field(default=None, alias="UserCode6", description="User-defined code 6")
    user_code7: int | str | None = Field(default=None, alias="UserCode7", description="User-defined code 7")
    user_code8: int | str | None = Field(default=None, alias="UserCode8", description="User-defined code 8")
    user_code9: int | str | None = Field(default=None, alias="UserCode9", description="User-defined code 9")

class StudentsCreateStudentInformationCreateResponse(AeriesModel):
    """Response model for `students.create_student_information_create`."""
    pass

class StudentsCreateStudentInformationUpdateResponse(AeriesModel):
    """Response model for `students.create_student_information_update`."""
    pass

class StudentsCreateUpdateAddressResponse(AeriesModel):
    """Response model for `students.create_update_address`."""
    pass

class StudentsGetStudentInformationExtendedResponse(AeriesModel):
    """Response model for `students.get_student_information_extended`."""
    birth_city: str | None = Field(default=None, alias="BirthCity", description="The city name where the student was born")
    birth_country_code: int | str | None = Field(default=None, alias="BirthCountryCode", description="The country code where the student was born")
    birth_state_code: int | str | None = Field(default=None, alias="BirthStateCode", description="The state or province in the US, Canada, or Mexico where the student was born")
    course_completion_csu: str | None = Field(default=None, alias="CourseCompletionCSU", description="The indicator for if this student has completed the course sequence for entrance into the CA State University (CSU) system")
    course_completion_uc: str | None = Field(default=None, alias="CourseCompletionUC", description="The indicator for if this student has completed the course sequence for entrance into the University of CA (UC) system")
    date_redesignated_fluent_english_proficient: str | None = Field(default=None, alias="DateRedesignatedFluentEnglishProficient", description="The Date the Student was redesignated/reclassified as Fluent English Proficient from an English Learner")
    district_mobility: str | None = Field(default=None, alias="DistrictMobility", description="The 'District Mobility' - the grade level the student entered this District during the most recent span of contiguous enrollment.")
    end_of_year_status_code: int | str | None = Field(default=None, alias="EndOfYearStatusCode", description="The End of Year Status Code for a student. This is populated at the end of the year when a student is going to be active through the last day of school but will leave the school over the summer and not be returning next school year.")
    english_learner_end_date: str | None = Field(default=None, alias="EnglishLearnerEndDate", description="The date the student was reclassified to no longer be an English Learner")
    english_learner_program_code: int | str | None = Field(default=None, alias="EnglishLearnerProgramCode", description="English Learner Program Code")
    english_learner_service_code: int | str | None = Field(default=None, alias="EnglishLearnerServiceCode", description="English Learner Services Received Code")
    english_learner_start_date: str | None = Field(default=None, alias="EnglishLearnerStartDate", description="The date the student began receiving English Learner services")
    expected_graduation_date: str | None = Field(default=None, alias="ExpectedGraduationDate", description="The Expected Graduation Date for this Student. This field is normally inconsistently populated as it is no longer required by CALPADS.")
    graduation_cohort: str | None = Field(default=None, alias="GraduationCohort", description="Graduation Cohort : '2019-2020',")
    graduation_requirements_track: str | None = Field(default=None, alias="GraduationRequirementsTrack", description="The Graduation Requirements Track for a student")
    home_language_survey_adult_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyAdultLanguageCode", description="From the Home Language Survey (HLS) - The language spoken most frequently by adults at home")
    home_language_survey_first_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyFirstLanguageCode", description="From the Home Language Survey (HLS) - The language first spoken by the student growing up")
    home_language_survey_home_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyHomeLanguageCode", description="From the Home Language Survey (HLS) - The language spoken most frequently at home by the student")
    home_language_survey_primary_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyPrimaryLanguageCode", description="From the Home Language Survey (HLS) - The language primarily spoken by the student")
    inter_intra_district_state_code: int | str | None = Field(default=None, alias="InterIntraDistrictStateCode", description="The Inter/Intra-District Transfer State Code for a student")
    inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="InterIntraDistrictTransferCode", description="The Inter/Intra-District Transfer Code for a student")
    initial_ninth_grade_entry_year: str | None = Field(default=None, alias="InitialNinthGradeEntryYear", description="Initial Ninth Grade Entry Year")
    long_term_english_learner_code: int | str | None = Field(default=None, alias="LongTermEnglishLearnerCode", description="Student Identified as a Long Term English Learner")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    qualified_csu: str | None = Field(default=None, alias="QualifiedCSU", description="The indicator for if this student has qualified for entrance into the CA State University (CSU) system")
    qualified_uc: str | None = Field(default=None, alias="QualifiedUC", description="The indicator for if this student has qualified for entrance into the University of CA (UC) system")
    record_added_date_time: str | None = Field(default=None, alias="RecordAddedDateTime", description="The Date/Time the student record was added to the system.")
    record_added_system: str | None = Field(default=None, alias="RecordAddedSystem", description="The system used to add this student record.")
    safe_schools_act_violation_date: str | None = Field(default=None, alias="SafeSchoolsActViolationDate", description="The Safe Schools Act Violation Date for this Student. I.e., the date the student violated a 'Violent' 48900 Ed Code.")
    scheduling_group: str | None = Field(default=None, alias="SchedulingGroup", description="The Scheduling Group for a student")
    birthdate_verification_method_code: str | None = Field(default=None, alias="BirthdateVerificationMethodCode", description="The Birthdate Verification Method Code")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code for this student")
    school_completion_date: str | None = Field(default=None, alias="SchoolCompletionDate", description="The School Completion Date for this Student. For High Schools, this is the Graduation Date.")
    school_completion_status_code: int | str | None = Field(default=None, alias="SchoolCompletionStatusCode", description="The Completion Status Code for this student from the current school. For High Schools, this is the Graduation Status Code.")
    school_mobility: str | None = Field(default=None, alias="SchoolMobility", description="The 'School Mobility' - the grade level the student entered this school during the most recent span of contiguous enrollment.")
    state_school_enter_date: str | None = Field(default=None, alias="StateSchoolEnterDate", description="The Date the Student first entered a school in the current state")
    state_student_id: str | None = Field(default=None, alias="StateStudentID", description="The State Student ID (SSID) for this Student")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-level Aeries Student Number for this student")
    summer_withdrawal_reason_code: int | str | None = Field(default=None, alias="SummerWithdrawalReasonCode", description="The Summer Withdrawal Reason Code for a student. This is populated at the beginning of the year when a student is found to have left the school during the summer and is not attending the first day of school.")
    us_enter_date: str | None = Field(default=None, alias="USEnterDate", description="The Date the Student first entered the US")
    us_school_enter_date: str | None = Field(default=None, alias="USSchoolEnterDate", description="The Date the Student first entered a US school to receive instruction")
    us_schools_less_than3_years: str | None = Field(default=None, alias="USSchoolsLessThan3Years", description="The indicator for when a student has been enrolled in US Schools for less than 3 years. This is normally the definition of an 'Eligible Immigrant' for SNOR reporting.")
    years_as_english_learner: int | str | None = Field(default=None, alias="YearsAsEnglishLearner", description="The Number of Years the student has been or was identified as an English Learner")
    count_in_census_indicator: int | str | None = Field(default=None, alias="CountInCensusIndicator", description="")
    next_inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="NextInterIntraDistrictTransferCode", description="The Students' Inter/Intra District Transfer Code for Next Year")
    next_inter_intra_district_state_code: int | str | None = Field(default=None, alias="NextInterIntraDistrictStateCode", description="")
    summer_withdrawal_leave_date: str | None = Field(default=None, alias="SummerWithdrawalLeaveDate", description="The Date the Student withdrew from the District before the start of the School Year")
    summer_withdrawal_next_school: str | None = Field(default=None, alias="SummerWithdrawalNextSchool", description="Expected School of attendance after withdrawal")
    end_of_year_next_school: str | None = Field(default=None, alias="EndOfYearNextSchool", description="Next School")
    reporting_school_code: int | str | None = Field(default=None, alias="ReportingSchoolCode", description="The Students Reporting School")
    next_attendance_program_code_primary: int | str | None = Field(default=None, alias="NextAttendanceProgramCodePrimary", description="The Students Primary Enrollment Program for Next Year")
    next_attendance_program_code_additional1: int | str | None = Field(default=None, alias="NextAttendanceProgramCodeAdditional1", description="The Students' first Additional Enrollment Program for Next Year")
    next_attendance_program_code_additional2: int | str | None = Field(default=None, alias="NextAttendanceProgramCodeAdditional2", description="The Students' second Additional Enrollment Program for Next Year")
    home_language_survey_date: str | None = Field(default=None, alias="HomeLanguageSurveyDate", description="The Date the Parent filled out the Home Language Survey")

class StudentsGetStudentInformationExtendedGradeGradeLevelExtendedResponse(AeriesModel):
    """Response model for `students.get_student_information_extended_grade_grade_level_extended`."""
    birth_city: str | None = Field(default=None, alias="BirthCity", description="The city name where the student was born")
    birth_country_code: int | str | None = Field(default=None, alias="BirthCountryCode", description="The country code where the student was born")
    birth_state_code: int | str | None = Field(default=None, alias="BirthStateCode", description="The state or province in the US, Canada, or Mexico where the student was born")
    course_completion_csu: str | None = Field(default=None, alias="CourseCompletionCSU", description="The indicator for if this student has completed the course sequence for entrance into the CA State University (CSU) system")
    course_completion_uc: str | None = Field(default=None, alias="CourseCompletionUC", description="The indicator for if this student has completed the course sequence for entrance into the University of CA (UC) system")
    date_redesignated_fluent_english_proficient: str | None = Field(default=None, alias="DateRedesignatedFluentEnglishProficient", description="The Date the Student was redesignated/reclassified as Fluent English Proficient from an English Learner")
    district_mobility: str | None = Field(default=None, alias="DistrictMobility", description="The 'District Mobility' - the grade level the student entered this District during the most recent span of contiguous enrollment.")
    end_of_year_status_code: int | str | None = Field(default=None, alias="EndOfYearStatusCode", description="The End of Year Status Code for a student. This is populated at the end of the year when a student is going to be active through the last day of school but will leave the school over the summer and not be returning next school year.")
    english_learner_end_date: str | None = Field(default=None, alias="EnglishLearnerEndDate", description="The date the student was reclassified to no longer be an English Learner")
    english_learner_program_code: int | str | None = Field(default=None, alias="EnglishLearnerProgramCode", description="English Learner Program Code")
    english_learner_service_code: int | str | None = Field(default=None, alias="EnglishLearnerServiceCode", description="English Learner Services Received Code")
    english_learner_start_date: str | None = Field(default=None, alias="EnglishLearnerStartDate", description="The date the student began receiving English Learner services")
    expected_graduation_date: str | None = Field(default=None, alias="ExpectedGraduationDate", description="The Expected Graduation Date for this Student. This field is normally inconsistently populated as it is no longer required by CALPADS.")
    graduation_cohort: str | None = Field(default=None, alias="GraduationCohort", description="Graduation Cohort : '2019-2020',")
    graduation_requirements_track: str | None = Field(default=None, alias="GraduationRequirementsTrack", description="The Graduation Requirements Track for a student")
    home_language_survey_adult_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyAdultLanguageCode", description="From the Home Language Survey (HLS) - The language spoken most frequently by adults at home")
    home_language_survey_first_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyFirstLanguageCode", description="From the Home Language Survey (HLS) - The language first spoken by the student growing up")
    home_language_survey_home_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyHomeLanguageCode", description="From the Home Language Survey (HLS) - The language spoken most frequently at home by the student")
    home_language_survey_primary_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyPrimaryLanguageCode", description="From the Home Language Survey (HLS) - The language primarily spoken by the student")
    inter_intra_district_state_code: int | str | None = Field(default=None, alias="InterIntraDistrictStateCode", description="The Inter/Intra-District Transfer State Code for a student")
    inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="InterIntraDistrictTransferCode", description="The Inter/Intra-District Transfer Code for a student")
    initial_ninth_grade_entry_year: str | None = Field(default=None, alias="InitialNinthGradeEntryYear", description="Initial Ninth Grade Entry Year")
    long_term_english_learner_code: int | str | None = Field(default=None, alias="LongTermEnglishLearnerCode", description="Student Identified as a Long Term English Learner")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    qualified_csu: str | None = Field(default=None, alias="QualifiedCSU", description="The indicator for if this student has qualified for entrance into the CA State University (CSU) system")
    qualified_uc: str | None = Field(default=None, alias="QualifiedUC", description="The indicator for if this student has qualified for entrance into the University of CA (UC) system")
    record_added_date_time: str | None = Field(default=None, alias="RecordAddedDateTime", description="The Date/Time the student record was added to the system.")
    record_added_system: str | None = Field(default=None, alias="RecordAddedSystem", description="The system used to add this student record.")
    safe_schools_act_violation_date: str | None = Field(default=None, alias="SafeSchoolsActViolationDate", description="The Safe Schools Act Violation Date for this Student. I.e., the date the student violated a 'Violent' 48900 Ed Code.")
    scheduling_group: str | None = Field(default=None, alias="SchedulingGroup", description="The Scheduling Group for a student")
    birthdate_verification_method_code: str | None = Field(default=None, alias="BirthdateVerificationMethodCode", description="The Birthdate Verification Method Code")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code for this student")
    school_completion_date: str | None = Field(default=None, alias="SchoolCompletionDate", description="The School Completion Date for this Student. For High Schools, this is the Graduation Date.")
    school_completion_status_code: int | str | None = Field(default=None, alias="SchoolCompletionStatusCode", description="The Completion Status Code for this student from the current school. For High Schools, this is the Graduation Status Code.")
    school_mobility: str | None = Field(default=None, alias="SchoolMobility", description="The 'School Mobility' - the grade level the student entered this school during the most recent span of contiguous enrollment.")
    state_school_enter_date: str | None = Field(default=None, alias="StateSchoolEnterDate", description="The Date the Student first entered a school in the current state")
    state_student_id: str | None = Field(default=None, alias="StateStudentID", description="The State Student ID (SSID) for this Student")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-level Aeries Student Number for this student")
    summer_withdrawal_reason_code: int | str | None = Field(default=None, alias="SummerWithdrawalReasonCode", description="The Summer Withdrawal Reason Code for a student. This is populated at the beginning of the year when a student is found to have left the school during the summer and is not attending the first day of school.")
    us_enter_date: str | None = Field(default=None, alias="USEnterDate", description="The Date the Student first entered the US")
    us_school_enter_date: str | None = Field(default=None, alias="USSchoolEnterDate", description="The Date the Student first entered a US school to receive instruction")
    us_schools_less_than3_years: str | None = Field(default=None, alias="USSchoolsLessThan3Years", description="The indicator for when a student has been enrolled in US Schools for less than 3 years. This is normally the definition of an 'Eligible Immigrant' for SNOR reporting.")
    years_as_english_learner: int | str | None = Field(default=None, alias="YearsAsEnglishLearner", description="The Number of Years the student has been or was identified as an English Learner")
    count_in_census_indicator: int | str | None = Field(default=None, alias="CountInCensusIndicator", description="")
    next_inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="NextInterIntraDistrictTransferCode", description="The Students' Inter/Intra District Transfer Code for Next Year")
    next_inter_intra_district_state_code: int | str | None = Field(default=None, alias="NextInterIntraDistrictStateCode", description="")
    summer_withdrawal_leave_date: str | None = Field(default=None, alias="SummerWithdrawalLeaveDate", description="The Date the Student withdrew from the District before the start of the School Year")
    summer_withdrawal_next_school: str | None = Field(default=None, alias="SummerWithdrawalNextSchool", description="Expected School of attendance after withdrawal")
    end_of_year_next_school: str | None = Field(default=None, alias="EndOfYearNextSchool", description="Next School")
    reporting_school_code: int | str | None = Field(default=None, alias="ReportingSchoolCode", description="The Students Reporting School")
    next_attendance_program_code_primary: int | str | None = Field(default=None, alias="NextAttendanceProgramCodePrimary", description="The Students Primary Enrollment Program for Next Year")
    next_attendance_program_code_additional1: int | str | None = Field(default=None, alias="NextAttendanceProgramCodeAdditional1", description="The Students' first Additional Enrollment Program for Next Year")
    next_attendance_program_code_additional2: int | str | None = Field(default=None, alias="NextAttendanceProgramCodeAdditional2", description="The Students' second Additional Enrollment Program for Next Year")
    home_language_survey_date: str | None = Field(default=None, alias="HomeLanguageSurveyDate", description="The Date the Parent filled out the Home Language Survey")

class StudentsGetStudentInformationExtendedSnStudentNumberExtendedResponse(AeriesModel):
    """Response model for `students.get_student_information_extended_sn_student_number_extended`."""
    birth_city: str | None = Field(default=None, alias="BirthCity", description="The city name where the student was born")
    birth_country_code: int | str | None = Field(default=None, alias="BirthCountryCode", description="The country code where the student was born")
    birth_state_code: int | str | None = Field(default=None, alias="BirthStateCode", description="The state or province in the US, Canada, or Mexico where the student was born")
    course_completion_csu: str | None = Field(default=None, alias="CourseCompletionCSU", description="The indicator for if this student has completed the course sequence for entrance into the CA State University (CSU) system")
    course_completion_uc: str | None = Field(default=None, alias="CourseCompletionUC", description="The indicator for if this student has completed the course sequence for entrance into the University of CA (UC) system")
    date_redesignated_fluent_english_proficient: str | None = Field(default=None, alias="DateRedesignatedFluentEnglishProficient", description="The Date the Student was redesignated/reclassified as Fluent English Proficient from an English Learner")
    district_mobility: str | None = Field(default=None, alias="DistrictMobility", description="The 'District Mobility' - the grade level the student entered this District during the most recent span of contiguous enrollment.")
    end_of_year_status_code: int | str | None = Field(default=None, alias="EndOfYearStatusCode", description="The End of Year Status Code for a student. This is populated at the end of the year when a student is going to be active through the last day of school but will leave the school over the summer and not be returning next school year.")
    english_learner_end_date: str | None = Field(default=None, alias="EnglishLearnerEndDate", description="The date the student was reclassified to no longer be an English Learner")
    english_learner_program_code: int | str | None = Field(default=None, alias="EnglishLearnerProgramCode", description="English Learner Program Code")
    english_learner_service_code: int | str | None = Field(default=None, alias="EnglishLearnerServiceCode", description="English Learner Services Received Code")
    english_learner_start_date: str | None = Field(default=None, alias="EnglishLearnerStartDate", description="The date the student began receiving English Learner services")
    expected_graduation_date: str | None = Field(default=None, alias="ExpectedGraduationDate", description="The Expected Graduation Date for this Student. This field is normally inconsistently populated as it is no longer required by CALPADS.")
    graduation_cohort: str | None = Field(default=None, alias="GraduationCohort", description="Graduation Cohort : '2019-2020',")
    graduation_requirements_track: str | None = Field(default=None, alias="GraduationRequirementsTrack", description="The Graduation Requirements Track for a student")
    home_language_survey_adult_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyAdultLanguageCode", description="From the Home Language Survey (HLS) - The language spoken most frequently by adults at home")
    home_language_survey_first_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyFirstLanguageCode", description="From the Home Language Survey (HLS) - The language first spoken by the student growing up")
    home_language_survey_home_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyHomeLanguageCode", description="From the Home Language Survey (HLS) - The language spoken most frequently at home by the student")
    home_language_survey_primary_language_code: int | str | None = Field(default=None, alias="HomeLanguageSurveyPrimaryLanguageCode", description="From the Home Language Survey (HLS) - The language primarily spoken by the student")
    inter_intra_district_state_code: int | str | None = Field(default=None, alias="InterIntraDistrictStateCode", description="The Inter/Intra-District Transfer State Code for a student")
    inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="InterIntraDistrictTransferCode", description="The Inter/Intra-District Transfer Code for a student")
    initial_ninth_grade_entry_year: str | None = Field(default=None, alias="InitialNinthGradeEntryYear", description="Initial Ninth Grade Entry Year")
    long_term_english_learner_code: int | str | None = Field(default=None, alias="LongTermEnglishLearnerCode", description="Student Identified as a Long Term English Learner")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    qualified_csu: str | None = Field(default=None, alias="QualifiedCSU", description="The indicator for if this student has qualified for entrance into the CA State University (CSU) system")
    qualified_uc: str | None = Field(default=None, alias="QualifiedUC", description="The indicator for if this student has qualified for entrance into the University of CA (UC) system")
    record_added_date_time: str | None = Field(default=None, alias="RecordAddedDateTime", description="The Date/Time the student record was added to the system.")
    record_added_system: str | None = Field(default=None, alias="RecordAddedSystem", description="The system used to add this student record.")
    safe_schools_act_violation_date: str | None = Field(default=None, alias="SafeSchoolsActViolationDate", description="The Safe Schools Act Violation Date for this Student. I.e., the date the student violated a 'Violent' 48900 Ed Code.")
    scheduling_group: str | None = Field(default=None, alias="SchedulingGroup", description="The Scheduling Group for a student")
    birthdate_verification_method_code: str | None = Field(default=None, alias="BirthdateVerificationMethodCode", description="The Birthdate Verification Method Code")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code for this student")
    school_completion_date: str | None = Field(default=None, alias="SchoolCompletionDate", description="The School Completion Date for this Student. For High Schools, this is the Graduation Date.")
    school_completion_status_code: int | str | None = Field(default=None, alias="SchoolCompletionStatusCode", description="The Completion Status Code for this student from the current school. For High Schools, this is the Graduation Status Code.")
    school_mobility: str | None = Field(default=None, alias="SchoolMobility", description="The 'School Mobility' - the grade level the student entered this school during the most recent span of contiguous enrollment.")
    state_school_enter_date: str | None = Field(default=None, alias="StateSchoolEnterDate", description="The Date the Student first entered a school in the current state")
    state_student_id: str | None = Field(default=None, alias="StateStudentID", description="The State Student ID (SSID) for this Student")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-level Aeries Student Number for this student")
    summer_withdrawal_reason_code: int | str | None = Field(default=None, alias="SummerWithdrawalReasonCode", description="The Summer Withdrawal Reason Code for a student. This is populated at the beginning of the year when a student is found to have left the school during the summer and is not attending the first day of school.")
    us_enter_date: str | None = Field(default=None, alias="USEnterDate", description="The Date the Student first entered the US")
    us_school_enter_date: str | None = Field(default=None, alias="USSchoolEnterDate", description="The Date the Student first entered a US school to receive instruction")
    us_schools_less_than3_years: str | None = Field(default=None, alias="USSchoolsLessThan3Years", description="The indicator for when a student has been enrolled in US Schools for less than 3 years. This is normally the definition of an 'Eligible Immigrant' for SNOR reporting.")
    years_as_english_learner: int | str | None = Field(default=None, alias="YearsAsEnglishLearner", description="The Number of Years the student has been or was identified as an English Learner")
    count_in_census_indicator: int | str | None = Field(default=None, alias="CountInCensusIndicator", description="")
    next_inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="NextInterIntraDistrictTransferCode", description="The Students' Inter/Intra District Transfer Code for Next Year")
    next_inter_intra_district_state_code: int | str | None = Field(default=None, alias="NextInterIntraDistrictStateCode", description="")
    summer_withdrawal_leave_date: str | None = Field(default=None, alias="SummerWithdrawalLeaveDate", description="The Date the Student withdrew from the District before the start of the School Year")
    summer_withdrawal_next_school: str | None = Field(default=None, alias="SummerWithdrawalNextSchool", description="Expected School of attendance after withdrawal")
    end_of_year_next_school: str | None = Field(default=None, alias="EndOfYearNextSchool", description="Next School")
    reporting_school_code: int | str | None = Field(default=None, alias="ReportingSchoolCode", description="The Students Reporting School")
    next_attendance_program_code_primary: int | str | None = Field(default=None, alias="NextAttendanceProgramCodePrimary", description="The Students Primary Enrollment Program for Next Year")
    next_attendance_program_code_additional1: int | str | None = Field(default=None, alias="NextAttendanceProgramCodeAdditional1", description="The Students' first Additional Enrollment Program for Next Year")
    next_attendance_program_code_additional2: int | str | None = Field(default=None, alias="NextAttendanceProgramCodeAdditional2", description="The Students' second Additional Enrollment Program for Next Year")
    home_language_survey_date: str | None = Field(default=None, alias="HomeLanguageSurveyDate", description="The Date the Parent filled out the Home Language Survey")

class StudentsGetStudentDataChangesResponse(AeriesModel):
    """Response model for `students.get_student_data_changes`."""
    pass

class StudentsGetContactsResponse(AeriesModel):
    """Response model for `students.get_contacts`."""
    access_to_portal: str | None = Field(default=None, alias="AccessToPortal", description="Indicates whether the contact can access the Aeries Parent Portal")
    additional_communication_type_code1: int | str | None = Field(default=None, alias="AdditionalCommunicationTypeCode1", description="Additional Contact 1 Type")
    additional_communication_type_code2: int | str | None = Field(default=None, alias="AdditionalCommunicationTypeCode2", description="Additional Contact 2 Type")
    additional_communication_type_code3: int | str | None = Field(default=None, alias="AdditionalCommunicationTypeCode3", description="Additional Contact 3 Type")
    additional_communication_type_code4: int | str | None = Field(default=None, alias="AdditionalCommunicationTypeCode4", description="Additional Contact 4 Type")
    additional_communication_detail1: int | str | None = Field(default=None, alias="AdditionalCommunicationDetail1", description="Additional Contact 1 Number")
    additional_communication_detail2: int | str | None = Field(default=None, alias="AdditionalCommunicationDetail2", description="Additional Contact 2 Number")
    additional_communication_detail3: int | str | None = Field(default=None, alias="AdditionalCommunicationDetail3", description="Additional Contact 3 Number")
    additional_communication_detail4: int | str | None = Field(default=None, alias="AdditionalCommunicationDetail4", description="Additional Contact 4 Number")
    address: str | None = Field(default=None, alias="Address", description="The street address of this contact")
    address_city: str | None = Field(default=None, alias="AddressCity", description="The city")
    address_state: str | None = Field(default=None, alias="AddressState", description="The state abbreviation")
    address_zip_code: int | str | None = Field(default=None, alias="AddressZipCode", description="The zip code")
    address_zip_ext: int | str | None = Field(default=None, alias="AddressZipExt", description="The zip code extension")
    address_type_code: int | str | None = Field(default=None, alias="AddressTypeCode", description="Address Type")
    address_verification_date: str | None = Field(default=None, alias="AddressVerificationDate", description="Address Verification Date")
    administrative_lock_code: int | str | None = Field(default=None, alias="AdministrativeLockCode", description="Contact record is locked for editing")
    attendance_notification: str | None = Field(default=None, alias="AttendanceNotification", description="Should the Contact receive Attendance Notifications?")
    birthdate: str | None = Field(default=None, alias="Birthdate", description="Contact Birthdate")
    cell_phone: int | str | None = Field(default=None, alias="CellPhone", description="The contact’s mobile phone number")
    comments: str | None = Field(default=None, alias="Comments", description="A free-text comment for this contact")
    contact_order: str | None = Field(default=None, alias="ContactOrder", description="The order in which this contact displays in Aeries")
    correspondence_language_code: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode", description="The language in which this contact prefers to receive correspondence")
    educational_rights_holder: str | None = Field(default=None, alias="EducationalRightsHolder", description="Educational Rights Holder")
    email_address: str | None = Field(default=None, alias="EmailAddress", description="The email address of this contact")
    employer_location: str | None = Field(default=None, alias="EmployerLocation", description="The location of this contact’s employer")
    employer_name: str | None = Field(default=None, alias="EmployerName", description="The name of this contact’s employer")
    enrolled_the_student_indicator: str | None = Field(default=None, alias="EnrolledTheStudentIndicator", description="If this is the Contact who Enrolled the Student in School")
    fingerprint_status_code: int | str | None = Field(default=None, alias="FingerprintStatusCode", description="Whether a Fingerprint has been obtained or not")
    fingerprint_date: str | None = Field(default=None, alias="FingerprintDate", description="Date Fingerprint submitted")
    first_name: str | None = Field(default=None, alias="FirstName", description="The contact’s first name")
    home_phone: int | str | None = Field(default=None, alias="HomePhone", description="The contact’s home phone number")
    last_name: str | None = Field(default=None, alias="LastName", description="The contact’s last name")
    lives_with_student_indicator: str | None = Field(default=None, alias="LivesWithStudentIndicator", description="Indicates whether the student lives with this contact")
    mailing_name: str | None = Field(default=None, alias="MailingName", description="The name for this contact that should appear on mailing labels")
    mail_tag_code: int | str | None = Field(default=None, alias="MailTagCode", description="Should Contact receive a copy of mail?")
    middle_name: str | None = Field(default=None, alias="MiddleName", description="The contact’s middle name")
    military_branch_code: int | str | None = Field(default=None, alias="MilitaryBranchCode", description="If this contact is in the military, the code indicates the branch of service")
    military_rank_code: int | str | None = Field(default=None, alias="MilitaryRankCode", description="If this contact is in the military, the code indicates the rank")
    military_status_code: int | str | None = Field(default=None, alias="MilitaryStatusCode", description="If this contact is/was in the military, the code indicates this contact’s military service status")
    military_supervisor_name: str | None = Field(default=None, alias="MilitarySupervisorName", description="If this contact is/was in the military, the name of the military supervisor")
    military_supervisor_phone: int | str | None = Field(default=None, alias="MilitarySupervisorPhone", description="If this contact is/was in the military, the phone number of the military supervisor")
    military_user_field_code1: int | str | None = Field(default=None, alias="MilitaryUserFieldCode1", description="Military User Code 1")
    military_user_field_code2: int | str | None = Field(default=None, alias="MilitaryUserFieldCode2", description="Military User Code 2")
    military_user_field_code3: int | str | None = Field(default=None, alias="MilitaryUserFieldCode3", description="Military User Code 3")
    military_user_field_code4: int | str | None = Field(default=None, alias="MilitaryUserFieldCode4", description="Military User Code 4")
    military_user_field_code5: int | str | None = Field(default=None, alias="MilitaryUserFieldCode5", description="Military User Code 5")
    misc_code: int | str | None = Field(default=None, alias="MiscCode", description="Record Type")
    name_prefix: str | None = Field(default=None, alias="NamePrefix", description="The name prefix for this contact")
    name_suffix: str | None = Field(default=None, alias="NameSuffix", description="The name suffix for this contact")
    notification_preference_code: int | str | None = Field(default=None, alias="NotificationPreferenceCode", description="Indicates the Aeries Communications notification preference of this contact")
    occupation: str | None = Field(default=None, alias="Occupation", description="Contacts' Occupation")
    pager: int | str | None = Field(default=None, alias="Pager", description="The Contact’s pager number")
    portal_account_id: int | str | None = Field(default=None, alias="PortalAccountID", description="The Portal Account ID value when contact email (CON.EM) matches a portal account email (PWA.EM). A value of zero will return when no CON.EM matches .EM.")
    primary_contact: str | None = Field(default=None, alias="PrimaryContact", description="Is this the Primary Contact for the Student?")
    primary_contact1_field: str | None = Field(default=None, alias="PrimaryContact1Field", description="Primary Contact 1 Phone linked to Student Demographics")
    primary_contact2_field: str | None = Field(default=None, alias="PrimaryContact2Field", description="Primary Contact 2 Phone linked to Student Demographics")
    primary_contact1_description: str | None = Field(default=None, alias="PrimaryContact1Description", description="Primary Contact 1 Phone Description")
    primary_contact2_description: str | None = Field(default=None, alias="PrimaryContact2Description", description="Primary Contact 2 Phone Description")
    red_flag: bool | None = Field(default=None, alias="RedFlag", description="Indicates whether the contact has been red-flagged")
    relationship_to_student_code: int | str | None = Field(default=None, alias="RelationshipToStudentCode", description="A code indicating the contact’s relationship to the student")
    record_added_date: str | None = Field(default=None, alias="RecordAddedDate", description="Date Record Added")
    record_type: str | None = Field(default=None, alias="RecordType", description="")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    sequence_number: int | str | None = Field(default=None, alias="SequenceNumber", description="The sequence number makes up the primary key of the Contacts table and has no independent meaning.")
    student_id: str | None = Field(default=None, alias="StudentID", description="Student ID")
    work_phone: int | str | None = Field(default=None, alias="WorkPhone", description="The contact’s work phone number")
    work_phone_ext: str | None = Field(default=None, alias="WorkPhoneExt", description="The contact’s work phone extension")
    tuberculosis_test_status_code: int | str | None = Field(default=None, alias="TuberculosisTestStatusCode", description="Status of the Contacts' TB test - Pass/Fail/Pending")
    tuberculosis_test_expiration_date: str | None = Field(default=None, alias="TuberculosisTestExpirationDate", description="TB Test Expiration Date")
    user_code1: int | str | None = Field(default=None, alias="UserCode1", description="User Code 1")
    user_code2: int | str | None = Field(default=None, alias="UserCode2", description="User Code 2")
    user_code3: int | str | None = Field(default=None, alias="UserCode3", description="User Code 3")
    user_code4: int | str | None = Field(default=None, alias="UserCode4", description="User Code 4")
    user_code5: int | str | None = Field(default=None, alias="UserCode5", description="User Code 5")
    user_code6: int | str | None = Field(default=None, alias="UserCode6", description="User Code 6")
    user_code7: int | str | None = Field(default=None, alias="UserCode7", description="User Code 7")
    user_code8: int | str | None = Field(default=None, alias="UserCode8", description="User Code 8")

class StudentsCreateContactsCreateResponse(AeriesModel):
    """Response model for `students.create_contacts_create`."""
    pass

class StudentsGetProgramsResponse(AeriesModel):
    """Response model for `students.get_programs`."""
    eligibility_end_date: str | None = Field(default=None, alias="EligibilityEndDate", description="ProgramCode")
    program_code: int | str | None = Field(default=None, alias="ProgramCode", description="")
    value_127: str | None = Field(default=None, alias="127", description="")
    value_101: str | None = Field(default=None, alias="101", description="")
    value_144: str | None = Field(default=None, alias="144", description="")
    value_181: str | None = Field(default=None, alias="181", description="")
    value_182: str | None = Field(default=None, alias="182", description="")
    all_others: str | None = Field(default=None, alias="All Others", description="")
    eligibility_start_date: str | None = Field(default=None, alias="EligibilityStartDate", description="ProgramCode")
    participation_end_date: str | None = Field(default=None, alias="ParticipationEndDate", description="ProgramCode")
    participation_start_date: str | None = Field(default=None, alias="ParticipationStartDate", description="ProgramCode")
    program: int | str | None = Field(default=None, alias="Program", description="ProgramCode")
    gate: str | None = Field(default=None, alias="GATE", description="127")
    value_504: str | None = Field(default=None, alias="504", description="101")
    special_education: str | None = Field(default=None, alias="Special Education", description="144")
    nslp_free: str | None = Field(default=None, alias="NSLP Free", description="181")
    nslp_reduced: str | None = Field(default=None, alias="NSLP Reduced", description="182")
    program_description: str | None = Field(default=None, alias="ProgramDescription", description="Table")
    table: str | None = Field(default=None, alias="Table", description="")
    gte: str | None = Field(default=None, alias="GTE", description="")
    fof: str | None = Field(default=None, alias="FOF", description="")
    cse: str | None = Field(default=None, alias="CSE", description="")
    fre_cd_f: str | None = Field(default=None, alias="FRE.CD = “F”", description="")
    fre_cd_r: str | None = Field(default=None, alias="FRE.CD = “R”", description="")
    pgm_all_others: str | None = Field(default=None, alias="PGM (All Others)", description="")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")

class StudentsGetTestScoresResponse(AeriesModel):
    """Response model for `students.get_test_scores`."""
    grade_level: str | None = Field(default=None, alias="GradeLevel", description="The student’s grade level when the test was taken")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    test_score: str | None = Field(default=None, alias="TestScore", description="Depending on the test, a single result can have multiple score types. For each nonzero value, a TestScore element will be included in the Scores container.")
    sequence_number: int | str | None = Field(default=None, alias="SequenceNumber", description="The sequence number makes up the primary key of the Test Scores table and has no independent meaning")
    test_date: str | None = Field(default=None, alias="TestDate", description="The date the test was taken")
    test_description: str | None = Field(default=None, alias="TestDescription", description="The description of the Test Part")
    test_id: str | None = Field(default=None, alias="TestID", description="The ID of the test. Ex: SBAC, ELPAC")
    test_part: str | None = Field(default=None, alias="TestPart", description="A numeric value to indicate which part of the test this Test Score result represents. Many standardized tests have multiple parts, such as Math and English/Language Arts.")
    test_source: str | None = Field(default=None, alias="TestSource", description="The source of this test result in Aeries. This may be blank. Other valid values include: LOC = Local Administration RT = Records Transfer VND = Testing Vendor")
    test_type: int | str | None = Field(default=None, alias="TestType", description="The type of test. Codes are set by the District.")
    testing_administration: str | None = Field(default=None, alias="TestingAdministration", description="The testing administration during which this test was taken. Depending on the test, this value may be in one of several formats. The most common are as follows: SPRG16 = Spring 2016. This format is used for tests that are typically administered only once per year in the spring term. 0916 = September 2016. This format is used for tests that are administered several times throughout the school year.")

class StudentsGetUpdateTestScoresResponse(AeriesModel):
    """Response model for `students.get_update_test_scores`."""
    pass

class StudentsGetCollegeEntranceTestScoresResponse(AeriesModel):
    """Response model for `students.get_college_entrance_test_scores`."""
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    overall_score: str | None = Field(default=None, alias="OverallScore", description="The overall score achieved on the test")
    code: int | str | None = Field(default=None, alias="Code", description="The code representing this subtest. See note below*")
    score: str | None = Field(default=None, alias="Score", description="The score achieved on this subtest")
    test_date: str | None = Field(default=None, alias="TestDate", description="The date the test was taken")
    test_name: str | None = Field(default=None, alias="TestName", description="The name of the test. Ex: ACT, SAT I, SAT II, AP")
    test_source_code: int | str | None = Field(default=None, alias="TestSourceCode", description="Test Source")
    test_type_code: int | str | None = Field(default=None, alias="TestTypeCode", description="Test Type")
    college_and_career_readiness_english_benchmark_indicato_r: str | None = Field(default=None, alias="CollegeAndCareerReadinessEnglishBenchmarkIndicato r", description="College And Career Readiness English Benchmark Indicator - PSAT")
    college_and_career_readiness_math_benchmark_indicator: str | None = Field(default=None, alias="CollegeAndCareerReadinessMathBenchmarkIndicator", description="College And Career Readiness Math Benchmark Indicator - PSAT")
    grade_level: str | None = Field(default=None, alias="GradeLevel", description="Grade Level - IB")

class StudentsGetAssertiveDisciplineResponse(AeriesModel):
    """Response model for `students.get_assertive_discipline`."""
    approximate_time_code: str | None = Field(default=None, alias="ApproximateTimeCode", description="The approximate time the incident occurred")
    comment: str | None = Field(default=None, alias="Comment", description="A comment describing the incident")
    demerits: int | str | None = Field(default=None, alias="Demerits", description="The number of demerits the student received for the incident")
    exact_time: str | None = Field(default=None, alias="ExactTime", description="The exact time the incident occurred")
    incident_date: str | None = Field(default=None, alias="IncidentDate", description="The date the incident occurred")
    incident_id: str | None = Field(default=None, alias="IncidentID", description="The Incident ID. This ID is used to link student Assertive Discipline records pertaining to the same incident (i.e., if two or more students were involved in the same incident, the Incident ID will be the same on those records).")
    initials: str | None = Field(default=None, alias="Initials", description="The initials of the staff member entering the record")
    instructional_support_indicator: str | None = Field(default=None, alias="InstructionalSupportIndicator", description="For special education students, indicates whether instructional support was provided during a suspension or expulsion resulting from this incident")
    is_substitute_teacher_referral: str | None = Field(default=None, alias="IsSubstituteTeacherReferral", description="Indicates whether the incident was referred by a substitute teacher")
    location_code: int | str | None = Field(default=None, alias="LocationCode", description="The location where the incident occurred")
    possible_motivation_code: int | str | None = Field(default=None, alias="PossibleMotivationCode", description="The student’s possible motivation for the incident")
    pre_referral_intervention_code1: int | str | None = Field(default=None, alias="PreReferralInterventionCode1", description="A first intervention that was attempted prior to making the disciplinary referral")
    pre_referral_intervention_code2: int | str | None = Field(default=None, alias="PreReferralInterventionCode2", description="A second intervention that was attempted prior to making the disciplinary referral")
    pre_referral_intervention_code3: int | str | None = Field(default=None, alias="PreReferralInterventionCode3", description="A third intervention that was attempted prior to making the disciplinary referral")
    school_of_incident_code: int | str | None = Field(default=None, alias="SchoolOfIncidentCode", description="The Aeries school code where the incident occurred")
    sequence_number: int | str | None = Field(default=None, alias="SequenceNumber", description="The sequence number is part of the primary key. It has no independent meaning.")
    staff_referral: str | None = Field(default=None, alias="StaffReferral", description="The staff member who made the referral")
    referred_by_other: str | None = Field(default=None, alias="ReferredByOther", description="Other referrer")
    user_code1: int | str | None = Field(default=None, alias="UserCode1", description="User-defined code 1")
    user_code2: int | str | None = Field(default=None, alias="UserCode2", description="User-defined code 2")
    user_code3: int | str | None = Field(default=None, alias="UserCode3", description="User-defined code 3")
    user_code4: int | str | None = Field(default=None, alias="UserCode4", description="User-defined code 4")
    user_code5: int | str | None = Field(default=None, alias="UserCode5", description="User-defined code 5")
    user_code6: int | str | None = Field(default=None, alias="UserCode6", description="User-defined code 6")
    user_code7: int | str | None = Field(default=None, alias="UserCode7", description="User-defined code 7")
    user_code8: int | str | None = Field(default=None, alias="UserCode8", description="User-defined code 8")
    violation_code1: int | str | None = Field(default=None, alias="ViolationCode1", description="The first violation committed in this incident (the first should be the most severe)")
    violation_code2: int | str | None = Field(default=None, alias="ViolationCode2", description="The second violation committed in this incident")
    violation_code3: int | str | None = Field(default=None, alias="ViolationCode3", description="The third violation committed in this incident")
    violation_code4: int | str | None = Field(default=None, alias="ViolationCode4", description="The fourth violation committed in this incident")
    violation_code5: int | str | None = Field(default=None, alias="ViolationCode5", description="The fifth violation committed in this incident")
    weapon_type_code: int | str | None = Field(default=None, alias="WeaponTypeCode", description="The type of weapon used in this incident")
    short_description: str | None = Field(default=None, alias="ShortDescription", description="Short Description of the Incident")
    assigned_days: str | None = Field(default=None, alias="AssignedDays", description="Days assigned to the Disciplinary Action, ie Days of Suspension")
    assigned_hours: str | None = Field(default=None, alias="AssignedHours", description="Hours assigned to the Disciplinary Action")
    assigned_start_date: str | None = Field(default=None, alias="AssignedStartDate", description="Assigned Start Date of Disciplinary Action")
    assigned_end_date: str | None = Field(default=None, alias="AssignedEndDate", description="Assigned End Date of Disciplinary Action")
    assigned_return_date: str | None = Field(default=None, alias="AssignedReturnDate", description="Student Assigned Return Date")
    reason_for_difference_code: str | None = Field(default=None, alias="ReasonForDifferenceCode", description="Code for the reason the Assigned date/time to serve a Disciplinary Action differs from the actual date/time served")
    disciplinary_assignment_schoolcode: int | str | None = Field(default=None, alias="DisciplinaryAssignmentSchoolcode", description="School that Assigned the Disciplinary Action")

class StudentsGetDisciplineResponse(AeriesModel):
    """Response model for `students.get_discipline`."""
    sequence_number: int | str | None = Field(default=None, alias="SequenceNumber", description="The sequence number is part of the primary key. It has no independent meaning.")
    incident_date: str | None = Field(default=None, alias="IncidentDate", description="The date the incident occurred")
    violation_code1: int | str | None = Field(default=None, alias="ViolationCode1", description="The violation committed in this incident")
    comment: str | None = Field(default=None, alias="Comment", description="A comment describing the incident")
    school_of_incident_code: int | str | None = Field(default=None, alias="SchoolOfIncidentCode", description="The Aeries school code where the incident occurred")
    staff_id: str | None = Field(default=None, alias="StaffID", description="The staff member who reported the incident or entered the incident into Aeries")
    user_created: str | None = Field(default=None, alias="UserCreated", description="The user who first created the discipline record")
    last_update_by: str | None = Field(default=None, alias="LastUpdateBy", description="The user who last updated the discipline record")
    last_update_date: str | None = Field(default=None, alias="LastUpdateDate", description="The last date the discipline record was updated")
    status: int | str | None = Field(default=None, alias="Status", description="The status code of the incident")
    exact_time: str | None = Field(default=None, alias="ExactTime", description="The date the incident occurred")
    location: str | None = Field(default=None, alias="Location", description="The location where the incident occurred")
    possible_motivation: str | None = Field(default=None, alias="PossibleMotivation", description="The possible motivation for the incident")
    consequence: str | None = Field(default=None, alias="Consequence", description="The consequence of the incident")

class StudentsGetDistrictSupplementalStudentDataResponse(AeriesModel):
    """Response model for `students.get_district_supplemental_student_data`."""
    pass

class StudentsGetSchoolSupplementalStudentDataResponse(AeriesModel):
    """Response model for `students.get_school_supplemental_student_data`."""
    pass

class StudentsGetFeesAndFinesResponse(AeriesModel):
    """Response model for `students.get_fees_and_fines`."""
    amount_charged: str | None = Field(default=None, alias="AmountCharged", description="The dollar amount of the Fee")
    amount_paid: str | None = Field(default=None, alias="AmountPaid", description="The dollar amount that has been paid toward the Fee")
    comment: str | None = Field(default=None, alias="Comment", description="A comment or note that the school has entered about this Fee")
    date_charged: str | None = Field(default=None, alias="DateCharged", description="The date the Fee was charged")
    date_paid: str | None = Field(default=None, alias="DatePaid", description="The date the Fee was paid")
    fee_code: int | str | None = Field(default=None, alias="FeeCode", description="A code representing the reason for the Fee")
    letter_count: int | str | None = Field(default=None, alias="LetterCount", description="The school can send Fee Letters to remind/warn students and parents about unpaid Fees. This is the number of such letters that have been sent pertaining to this Fee.")
    receipt_number: int | str | None = Field(default=None, alias="ReceiptNumber", description="When a Fee is paid, the school can store the receipt number for the payment")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code of the school where the Fee was charged")
    sequence_number: int | str | None = Field(default=None, alias="SequenceNumber", description="The sequence number is part of the primary key. It has no independent meaning.")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")

class StudentsGetStudentPictureResponse(AeriesModel):
    """Response model for `students.get_student_picture`."""
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    file_extension: str | None = Field(default=None, alias="FileExtension", description="The original file extension of the photo (e.g., “jpg”)")
    file_size: str | None = Field(default=None, alias="FileSize", description="The size in bytes of the photo")
    raw_binary: str | None = Field(default=None, alias="RawBinary", description="A serialized byte array containing the student photo")
    school_year: str | None = Field(default=None, alias="SchoolYear", description="The school year the photo was taken (e.g., 2016 for the 2016-2017 school year)")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")

class StudentsGetStudentGroupsResponse(AeriesModel):
    """Response model for `students.get_student_groups`."""
    description: str | None = Field(default=None, alias="Description", description="The description of the group")
    expiration_date: str | None = Field(default=None, alias="ExpirationDate", description="The date the group expires. If the expiration date is populated and has passed, the group should be considered inactive.")
    group_id: str | None = Field(default=None, alias="GroupId", description="The unique identifier for the group")
    is_communication_group: str | None = Field(default=None, alias="IsCommunicationGroup", description="Indicates whether the group is synced with the Aeries Communication platform")
    confidential_group: str | None = Field(default=None, alias="ConfidentialGroup", description="Will indicate whether the group is a Confidential Group in ParentSquare.")
    name: str | None = Field(default=None, alias="Name", description="The name of the group")
    staff_id: str | None = Field(default=None, alias="StaffId", description="The staff ID of a staff member associated with the group")
    student_id: str | None = Field(default=None, alias="StudentId", description="The Student ID of a student who is a member of the group")

class GradesGetStudentGpAsResponse(AeriesModel):
    """Response model for `grades.get_student_gp_as`."""
    class_rank: str | None = Field(default=None, alias="ClassRank", description="The cumulative class rank based on the school’s selection of which GPA calculation to use")
    class_rank1012: str | None = Field(default=None, alias="ClassRank1012", description="The cumulative class rank based on the grades 10-12 Academic GPA")
    class_size: str | None = Field(default=None, alias="ClassSize", description="The class size including active and graduated students")
    credits_attempted: int | str | None = Field(default=None, alias="CreditsAttempted", description="The cumulative number of course credits attempted by the student")
    credits_completed: int | str | None = Field(default=None, alias="CreditsCompleted", description="The cumulative number of course credits completed by the student")
    gpa_csu_preliminary: str | None = Field(default=None, alias="GPA_CSU_Preliminary", description="The preliminary academic GPA for California State University entrance")
    gpa_cumulative_academic: str | None = Field(default=None, alias="GPA_CumulativeAcademic", description="The cumulative, weighted academic GPA (i.e., excludes all non-academic courses)")
    gpa_cumulative_academic1012: str | None = Field(default=None, alias="GPA_CumulativeAcademic1012", description="The cumulative, weighted academic GPA including only academic courses taken in grades 10-12")
    gpa_cumulative_academic1012_non_weighted: str | None = Field(default=None, alias="GPA_CumulativeAcademic1012NonWeighted", description="The cumulative, non-weighted academic GPA including only academic courses taken in grades 10-12")
    gpa_cumulative_academic_non_weighted: str | None = Field(default=None, alias="GPA_CumulativeAcademicNonWeighted", description="The cumulative, non-weighted academic GPA (i.e., excludes all non-academic courses)")
    gpa_cumulative_citizenship: str | None = Field(default=None, alias="GPA_CumulativeCitizenship", description="The cumulative “Citizenship GPA”")
    gpa_cumulative_total: str | None = Field(default=None, alias="GPA_CumulativeTotal", description="The cumulative, weighted total GPA (includes non-academic courses))")
    gpa_cumulative_total_non_weighted: str | None = Field(default=None, alias="GPA_CumulativeTotalNonWeighted", description="The cumulative, nonweighted total GPA (includes non-academic courses)")
    gpa_grade_reporting_academic: str | None = Field(default=None, alias="GPA_GradeReportingAcademic", description="The weighted, academic GPA calculated from the current marking period")
    gpa_grade_reporting_academic_non_weighted: str | None = Field(default=None, alias="GPA_GradeReportingAcademicNonWeighted", description="The non-weighted, academic GPA calculated from the current marking period")
    gpa_grade_reporting_citizenship: str | None = Field(default=None, alias="GPA_GradeReportingCitizenship", description="The “Citizenship GPA” calculated from the current marking period")
    gpa_grade_reporting_total: str | None = Field(default=None, alias="GPA_GradeReportingTotal", description="The weighted total GPA calculated from the current marking period")
    gpa_grade_reporting_total_non_weighted: str | None = Field(default=None, alias="GPA_GradeReportingTotalNonWeighted", description="The non-weighted total GPA calculated from the current marking period")
    gpa_uc_preliminary: str | None = Field(default=None, alias="GPA_UC_Preliminary", description="The preliminary academic GPA for University of California entrance")
    grade_points_cumulative: int | str | None = Field(default=None, alias="GradePointsCumulative", description="The number of grade points used to calculate UC and CSU GPAs")
    grade_reporting_class_rank: str | None = Field(default=None, alias="GradeReportingClassRank", description="The class rank, based on the school’s selection of which GPA calculation to use, calculated from the current marking period")
    grade_reporting_class_size: str | None = Field(default=None, alias="GradeReportingClassSize", description="The class size including active students only")
    grade_reporting_credits_attempted: int | str | None = Field(default=None, alias="GradeReportingCreditsAttempted", description="The number of course credits attempted by the student in the current marking period")
    grade_reporting_credits_completed: int | str | None = Field(default=None, alias="GradeReportingCreditsCompleted", description="The number of course credits completed by the student in the current marking period")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")

class GradesGetStudentGradesResponse(AeriesModel):
    """Response model for `grades.get_student_grades`."""
    pass

class GradesGetStudentReportCardsResponse(AeriesModel):
    """Response model for `grades.get_student_report_cards`."""
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    course_id: str | None = Field(default=None, alias="CourseID", description="The District course ID")
    course_title: str | None = Field(default=None, alias="CourseTitle", description="The title of the course")
    citizenship_code: int | str | None = Field(default=None, alias="CitizenshipCode", description="A code describing the student’s meeting of satisfactory citizenship for this marking period")
    comment1_code: int | str | None = Field(default=None, alias="Comment1Code", description="A comment chosen by the teacher for this student for this marking period from a list of pre-defined comments")
    comment2_code: int | str | None = Field(default=None, alias="Comment2Code", description="Additional comment")
    comment3_code: int | str | None = Field(default=None, alias="Comment3Code", description="Additional comment")
    credit: str | None = Field(default=None, alias="Credit", description="The credits earned by this student for this course during this marking period")
    mark: str | None = Field(default=None, alias="Mark", description="The mark (e.g., “A”, “B+”) received. Note: For the current marking period only, the respective field from GRD.M1 – M12 will be used instead")
    marking_period: str | None = Field(default=None, alias="MarkingPeriod", description="The marking period (1 – 12) for this grade reporting entry")
    section_number: int | str | None = Field(default=None, alias="SectionNumber", description="The master schedule section number for this report card course")
    total_absences: int | str | None = Field(default=None, alias="TotalAbsences", description="The total number of days the student was absent from this class during this marking period")
    total_days_enrolled: int | str | None = Field(default=None, alias="TotalDaysEnrolled", description="The total number of days the student was enrolled in this class during this marking period")
    total_days_of_suspension: int | str | None = Field(default=None, alias="TotalDaysOfSuspension", description="The total number of days the student was suspended from this class during this marking period")
    total_days_present: int | str | None = Field(default=None, alias="TotalDaysPresent", description="The total number of days the student was present in this class during this marking period")
    total_excused_absences: int | str | None = Field(default=None, alias="TotalExcusedAbsences", description="The total number of days the student had an excused absence from this class during this marking period")
    total_tardies: int | str | None = Field(default=None, alias="TotalTardies", description="The total number of days the student was tardy to this class during this marking period")
    total_un_excused_absences: int | str | None = Field(default=None, alias="TotalUnExcusedAbsences", description="The total number of days the student had an unexcused absence from this class during this marking period")
    work_habits_code: int | str | None = Field(default=None, alias="WorkHabitsCode", description="A code describing the student’s meeting of satisfactory work habits for this marking period")
    period: str | None = Field(default=None, alias="Period", description="The class period. For Flex Schools, Period will come from FTF.STI")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    teacher_number: int | str | None = Field(default=None, alias="TeacherNumber", description="The school-based teacher number")
    primary_staff_id: str | None = Field(default=None, alias="PrimaryStaffID", description="The Staff ID")
    hours: str | None = Field(default=None, alias="Hours", description="Hours")
    attendance_based_grades_indicator: str | None = Field(default=None, alias="AttendanceBasedGradesIndicator", description="Attendance Based Grades Indicator")

class GradesGetSchoolReportCardMarkingPeriodsResponse(AeriesModel):
    """Response model for `grades.get_school_report_card_marking_periods`."""
    is_current_marking_period: bool | None = Field(default=None, alias="IsCurrentMarkingPeriod", description="True or False. Indicates whether this marking period is the school’s current marking period.")
    long_description: str | None = Field(default=None, alias="LongDescription", description="The full description of the marking period")
    marking_period: str | None = Field(default=None, alias="MarkingPeriod", description="The marking period (1 – 12)")
    short_description: str | None = Field(default=None, alias="ShortDescription", description="The abbreviated description of the marking period. This is used as the column heading on the printed report card.")
    beginning_date: str | None = Field(default=None, alias="BeginningDate", description="Beginning Date of Marking Period")
    ending_date: str | None = Field(default=None, alias="EndingDate", description="Ending Date of Marking Period")
    state_reporting_code: int | str | None = Field(default=None, alias="StateReportingCode", description="State Reporting Code")

class GradesGetSchoolGraduationRequirementsResponse(AeriesModel):
    """Response model for `grades.get_school_graduation_requirements`."""
    graduation_requirement_track: str | None = Field(default=None, alias="GraduationRequirementTrack", description="The Graduation Track to which this requirement applies. Graduation Tracks can be used to establish different graduation requirements for specific groups of students and are also used to separate specific groups of students for class rank/size calculations.")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    required_credit_for10th_graders: int | str | None = Field(default=None, alias="RequiredCreditFor10thGraders", description="The number of course credits required in this subject area for students currently in grade 10")
    required_credit_for11th_graders: int | str | None = Field(default=None, alias="RequiredCreditFor11thGraders", description="The number of course credits required in this subject area for students currently in grade 11")
    required_credit_for12th_graders: int | str | None = Field(default=None, alias="RequiredCreditFor12thGraders", description="The number of course credits required in this subject area for students currently in grade 12")
    required_credit_for9th_graders: int | str | None = Field(default=None, alias="RequiredCreditFor9thGraders", description="The number of course credits required in this subject area for students currently in grade 9")
    subject_area_code: int | str | None = Field(default=None, alias="SubjectAreaCode", description="The subject area code (single character) for this requirement")
    subject_area_description: str | None = Field(default=None, alias="SubjectAreaDescription", description="The name/description of the subject area for this requirement")

class GradesGetStudentGraduationStatusSummaryResponse(AeriesModel):
    """Response model for `grades.get_student_graduation_status_summary`."""
    graduation_requirement_track: str | None = Field(default=None, alias="GraduationRequirementTrack", description="The Graduation Track to which this student belongs (if any). Graduation Tracks can be used to establish different graduation requirements for specific groups of students and are also used to separate specific groups of students for class rank/size calculations.")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    credits_completed: int | str | None = Field(default=None, alias="CreditsCompleted", description="The number of credits the student has completed in this subject area.")
    credits_currently_enrolled: int | str | None = Field(default=None, alias="CreditsCurrentlyEnrolled", description="The number of credits in this subject area in which the student is currently enrolled.")
    credits_needed: int | str | None = Field(default=None, alias="CreditsNeeded", description="The number of credits in this subject area that the student still needs.")
    credits_required: str | None = Field(default=None, alias="CreditsRequired", description="The credits required in this subject area based on the student’s grade level. Grade 9 = C4 Grade 10 = C3 Grade 11 = C2 Grade 12 = C1")
    subject_area_code: int | str | None = Field(default=None, alias="SubjectAreaCode", description="The subject area code (single character)")
    subject_area_description: str | None = Field(default=None, alias="SubjectAreaDescription", description="The name/description of the subject area")

class GradesGetStudentGraduationStatusSummaryGradeGradeLevelResponse(AeriesModel):
    """Response model for `grades.get_student_graduation_status_summary_grade_grade_level`."""
    graduation_requirement_track: str | None = Field(default=None, alias="GraduationRequirementTrack", description="The Graduation Track to which this student belongs (if any). Graduation Tracks can be used to establish different graduation requirements for specific groups of students and are also used to separate specific groups of students for class rank/size calculations.")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    credits_completed: int | str | None = Field(default=None, alias="CreditsCompleted", description="The number of credits the student has completed in this subject area.")
    credits_currently_enrolled: int | str | None = Field(default=None, alias="CreditsCurrentlyEnrolled", description="The number of credits in this subject area in which the student is currently enrolled.")
    credits_needed: int | str | None = Field(default=None, alias="CreditsNeeded", description="The number of credits in this subject area that the student still needs.")
    credits_required: str | None = Field(default=None, alias="CreditsRequired", description="The credits required in this subject area based on the student’s grade level. Grade 9 = C4 Grade 10 = C3 Grade 11 = C2 Grade 12 = C1")
    subject_area_code: int | str | None = Field(default=None, alias="SubjectAreaCode", description="The subject area code (single character)")
    subject_area_description: str | None = Field(default=None, alias="SubjectAreaDescription", description="The name/description of the subject area")

class GradesGetStudentTranscriptsResponse(AeriesModel):
    """Response model for `grades.get_student_transcripts`."""
    citizenship_mark: str | None = Field(default=None, alias="CitizenshipMark", description="The mark the student received for the meeting of satisfactory citizenship.")
    course_id: str | None = Field(default=None, alias="CourseID", description="The District course ID of the course taken")
    credit_attempted: int | str | None = Field(default=None, alias="CreditAttempted", description="The number of credits the student attempted")
    credit_completed: int | str | None = Field(default=None, alias="CreditCompleted", description="The number of credits the student earned")
    mark: str | None = Field(default=None, alias="Mark", description="The mark (e.g., “A”, “B+”) received.")
    repeat_tag_code: int | str | None = Field(default=None, alias="RepeatTagCode", description="If this record represents a repeated course, this code indicates whether the repeat counts toward the student’s total Credit Attempted, Credit Completed, and the GPA calculation.")
    school_taken_id: int | str | None = Field(default=None, alias="SchoolTakenID", description="An identifier for the school at which this course was taken. For courses taken within the current district, this will usually match the respective Aeries school code.")
    school_taken_name: str | None = Field(default=None, alias="SchoolTakenName", description="The name of the school at which this course was taken")
    school_taken_state_id: int | str | None = Field(default=None, alias="SchoolTakenStateID", description="The state school ID (e.g., CDS code) for the school at which this course was taken.")
    school_year: str | None = Field(default=None, alias="SchoolYear", description="The school year when the course was taken (e.g., “2016-2017”)")
    section_number: int | str | None = Field(default=None, alias="SectionNumber", description="The master schedule section number of the course taken")
    sequence_number: int | str | None = Field(default=None, alias="SequenceNumber", description="The sequence number is part of the primary key. It has no independent meaning.")
    staff_id: str | None = Field(default=None, alias="StaffID", description="The Aeries staff ID of the teacher who taught the course taken")
    student_grade: str | None = Field(default=None, alias="StudentGrade", description="The student’s grade level at the time the course was taken")
    term: str | None = Field(default=None, alias="Term", description="The term during which the course was taken")
    term_description: str | None = Field(default=None, alias="TermDescription", description="The description for the Term.")
    total_absences: int | str | None = Field(default=None, alias="TotalAbsences", description="The total number of days the student was absent from this class during the term taken")
    total_days_enrolled: int | str | None = Field(default=None, alias="TotalDaysEnrolled", description="The total number of days the student was enrolled in this class during the term taken")
    total_days_of_suspension: int | str | None = Field(default=None, alias="TotalDaysOfSuspension", description="The total number of days the student was suspended from this class during the term taken")
    total_days_present: int | str | None = Field(default=None, alias="TotalDaysPresent", description="The total number of days the student was present in this class during the term taken")
    total_excused_absences: int | str | None = Field(default=None, alias="TotalExcusedAbsences", description="The total number of days the student had an excused absence from this class during the term taken")
    total_tardies: int | str | None = Field(default=None, alias="TotalTardies", description="The total number of days the student was tardy to this class during the term taken")
    total_un_excused_absences: int | str | None = Field(default=None, alias="TotalUnExcusedAbsences", description="The total number of days the student had an unexcused absence from this class during the term taken")
    transcript_course_title: str | None = Field(default=None, alias="TranscriptCourseTitle", description="The title of the course to be printed on the transcript, if different from the District’s course title. This is typically populated when the course was taken at a different district so the other district’s exact course title can be used. This should generally be blank for courses taken inside the District.")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Student ID")
    school_code: int | str | None = Field(default=None, alias="School Code", description="The Aeries school code")
    hours: str | None = Field(default=None, alias="Hours", description="Hours for Alternative Education Schools")
    record_source: str | None = Field(default=None, alias="RecordSource", description="Record Source")
    dual_enrollment_credit_school_code: int | str | None = Field(default=None, alias="DualEnrollmentCreditSchoolCode", description="School of Credit for Dual Enrollment Courses")
    date_of_completion: str | None = Field(default=None, alias="DateOfCompletion", description="Date of Completion")
    college_credit_hours: str | None = Field(default=None, alias="CollegeCreditHours", description="College Credit Hours")
    pass_fail_credit_code: int | str | None = Field(default=None, alias="PassFailCreditCode", description="Pass/Fail Credit code")

class GradesGetValidMarksResponse(AeriesModel):
    """Response model for `grades.get_valid_marks`."""
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="School code the mark belongs to")
    mark: str | None = Field(default=None, alias="Mark", description="The grade mark value (e.g., 'A+', 'B', 'F')")
    non_honor_points: str | None = Field(default=None, alias="NonHonorPoints", description="Grade points for non-honor courses")
    honor_points: str | None = Field(default=None, alias="HonorPoints", description="Grade points for honor courses")
    count_as_attempted: int | str | None = Field(default=None, alias="CountAsAttempted", description="Whether this mark counts as credits attempted")
    count_as_completed: int | str | None = Field(default=None, alias="CountAsCompleted", description="Whether this mark counts as credits completed")
    count_in_gpa: int | str | None = Field(default=None, alias="CountInGPA", description="High end of percentage range for this mark")
    sequence_number: int | str | None = Field(default=None, alias="SequenceNumber", description="Display order for the mark")
    non_academic_points: str | None = Field(default=None, alias="NonAcademicPoints", description="Grade points for non-academic courses")
    low_percentage: str | None = Field(default=None, alias="LowPercentage", description="Low end of percentage range for this mark")
    high_percentage: str | None = Field(default=None, alias="HighPercentage", description="High end of percentage range for this mark")
    mark_type: int | str | None = Field(default=None, alias="MarkType", description="Mark type classification code")
    appoints: str | None = Field(default=None, alias="Appoints", description="Grade points for AP courses")

class AttendanceGetStudentEnrollmentHistoryResponse(AeriesModel):
    """Response model for `attendance.get_student_enrollment_history`."""
    academic_year: str | None = Field(default=None, alias="AcademicYear", description="The 4-digit academic year of this enrollment period; e.g., 2024 for the 2024-2025 academic year")
    attendance_program_code: int | str | None = Field(default=None, alias="AttendanceProgramCode", description="The specialized attendance program to which this student belonged during this enrollment period. Attendance programs are used to separate certain students’ attendance data in the monthly apportionment (ADA) calculations.")
    attendance_program_code_additional1: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional1", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    attendance_program_code_additional2: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional2", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    elementary_teacher_name: str | None = Field(default=None, alias="ElementaryTeacherName", description="For elementary schools, the display name of the teacher to whom the student was assigned during this enrollment period")
    elementary_teacher_number: int | str | None = Field(default=None, alias="ElementaryTeacherNumber", description="For elementary schools, the school-based teacher number of the teacher to whom the student was assigned during this enrollment period")
    enter_date: str | None = Field(default=None, alias="EnterDate", description="The start date of this enrollment period")
    exit_reason_code: int | str | None = Field(default=None, alias="ExitReasonCode", description="A coded value indicating the reason the enrollment period ended. These codes align with state reporting requirements.")
    grade: str | None = Field(default=None, alias="Grade", description="The student’s grade level during this enrollment period")
    inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="InterIntraDistrictTransferCode", description="The student’s interdistrict or intradistrict transfer status during this enrollment period")
    leave_date: str | None = Field(default=None, alias="LeaveDate", description="The end date of this enrollment period")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Permanent ID for the student")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code of the school where this enrollment took place")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-based Aeries student number assigned to the student during this enrollment period")
    track: str | None = Field(default=None, alias="Track", description="The student’s attendance track during this enrollment period")
    inter_intra_district_state_code: int | str | None = Field(default=None, alias="InterIntraDistrictStateCode", description="Inter/Intra District State Code")

class AttendanceGetStudentEnrollmentHistoryYearAcademicYearResponse(AeriesModel):
    """Response model for `attendance.get_student_enrollment_history_year_academic_year`."""
    academic_year: str | None = Field(default=None, alias="AcademicYear", description="The 4-digit academic year of this enrollment period; e.g., 2024 for the 2024-2025 academic year")
    attendance_program_code: int | str | None = Field(default=None, alias="AttendanceProgramCode", description="The specialized attendance program to which this student belonged during this enrollment period. Attendance programs are used to separate certain students’ attendance data in the monthly apportionment (ADA) calculations.")
    attendance_program_code_additional1: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional1", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    attendance_program_code_additional2: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional2", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    elementary_teacher_name: str | None = Field(default=None, alias="ElementaryTeacherName", description="For elementary schools, the display name of the teacher to whom the student was assigned during this enrollment period")
    elementary_teacher_number: int | str | None = Field(default=None, alias="ElementaryTeacherNumber", description="For elementary schools, the school-based teacher number of the teacher to whom the student was assigned during this enrollment period")
    enter_date: str | None = Field(default=None, alias="EnterDate", description="The start date of this enrollment period")
    exit_reason_code: int | str | None = Field(default=None, alias="ExitReasonCode", description="A coded value indicating the reason the enrollment period ended. These codes align with state reporting requirements.")
    grade: str | None = Field(default=None, alias="Grade", description="The student’s grade level during this enrollment period")
    inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="InterIntraDistrictTransferCode", description="The student’s interdistrict or intradistrict transfer status during this enrollment period")
    leave_date: str | None = Field(default=None, alias="LeaveDate", description="The end date of this enrollment period")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Permanent ID for the student")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code of the school where this enrollment took place")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-based Aeries student number assigned to the student during this enrollment period")
    track: str | None = Field(default=None, alias="Track", description="The student’s attendance track during this enrollment period")
    inter_intra_district_state_code: int | str | None = Field(default=None, alias="InterIntraDistrictStateCode", description="Inter/Intra District State Code")

class AttendanceGetStudentEnrollmentHistorySchoolsSchoolCodeEnrollmentStudentIdResponse(AeriesModel):
    """Response model for `attendance.get_student_enrollment_history_schools_school_code_enrollment_student_id`."""
    academic_year: str | None = Field(default=None, alias="AcademicYear", description="The 4-digit academic year of this enrollment period; e.g., 2024 for the 2024-2025 academic year")
    attendance_program_code: int | str | None = Field(default=None, alias="AttendanceProgramCode", description="The specialized attendance program to which this student belonged during this enrollment period. Attendance programs are used to separate certain students’ attendance data in the monthly apportionment (ADA) calculations.")
    attendance_program_code_additional1: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional1", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    attendance_program_code_additional2: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional2", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    elementary_teacher_name: str | None = Field(default=None, alias="ElementaryTeacherName", description="For elementary schools, the display name of the teacher to whom the student was assigned during this enrollment period")
    elementary_teacher_number: int | str | None = Field(default=None, alias="ElementaryTeacherNumber", description="For elementary schools, the school-based teacher number of the teacher to whom the student was assigned during this enrollment period")
    enter_date: str | None = Field(default=None, alias="EnterDate", description="The start date of this enrollment period")
    exit_reason_code: int | str | None = Field(default=None, alias="ExitReasonCode", description="A coded value indicating the reason the enrollment period ended. These codes align with state reporting requirements.")
    grade: str | None = Field(default=None, alias="Grade", description="The student’s grade level during this enrollment period")
    inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="InterIntraDistrictTransferCode", description="The student’s interdistrict or intradistrict transfer status during this enrollment period")
    leave_date: str | None = Field(default=None, alias="LeaveDate", description="The end date of this enrollment period")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Permanent ID for the student")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code of the school where this enrollment took place")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-based Aeries student number assigned to the student during this enrollment period")
    track: str | None = Field(default=None, alias="Track", description="The student’s attendance track during this enrollment period")
    inter_intra_district_state_code: int | str | None = Field(default=None, alias="InterIntraDistrictStateCode", description="Inter/Intra District State Code")

class AttendanceGetStudentEnrollmentHistorySchoolsSchoolCodeEnrollmentStudentIdYearAcademicYearResponse(AeriesModel):
    """Response model for `attendance.get_student_enrollment_history_schools_school_code_enrollment_student_id_year_academic_year`."""
    academic_year: str | None = Field(default=None, alias="AcademicYear", description="The 4-digit academic year of this enrollment period; e.g., 2024 for the 2024-2025 academic year")
    attendance_program_code: int | str | None = Field(default=None, alias="AttendanceProgramCode", description="The specialized attendance program to which this student belonged during this enrollment period. Attendance programs are used to separate certain students’ attendance data in the monthly apportionment (ADA) calculations.")
    attendance_program_code_additional1: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional1", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    attendance_program_code_additional2: int | str | None = Field(default=None, alias="AttendanceProgramCodeAdditional2", description="An additional specialized attendance program to which this student belonged during this enrollment period")
    elementary_teacher_name: str | None = Field(default=None, alias="ElementaryTeacherName", description="For elementary schools, the display name of the teacher to whom the student was assigned during this enrollment period")
    elementary_teacher_number: int | str | None = Field(default=None, alias="ElementaryTeacherNumber", description="For elementary schools, the school-based teacher number of the teacher to whom the student was assigned during this enrollment period")
    enter_date: str | None = Field(default=None, alias="EnterDate", description="The start date of this enrollment period")
    exit_reason_code: int | str | None = Field(default=None, alias="ExitReasonCode", description="A coded value indicating the reason the enrollment period ended. These codes align with state reporting requirements.")
    grade: str | None = Field(default=None, alias="Grade", description="The student’s grade level during this enrollment period")
    inter_intra_district_transfer_code: int | str | None = Field(default=None, alias="InterIntraDistrictTransferCode", description="The student’s interdistrict or intradistrict transfer status during this enrollment period")
    leave_date: str | None = Field(default=None, alias="LeaveDate", description="The end date of this enrollment period")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Permanent ID for the student")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code of the school where this enrollment took place")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-based Aeries student number assigned to the student during this enrollment period")
    track: str | None = Field(default=None, alias="Track", description="The student’s attendance track during this enrollment period")
    inter_intra_district_state_code: int | str | None = Field(default=None, alias="InterIntraDistrictStateCode", description="Inter/Intra District State Code")

class AttendanceGetStudentAttendanceResponse(AeriesModel):
    """Response model for `attendance.get_student_attendance`."""
    student_id: str | None = Field(default=None, alias="StudentID", description="Student ID")
    attendance_days: str | None = Field(default=None, alias="AttendanceDays", description="Array of Class Attendance Objects")
    all_day_attendance_code: int | str | None = Field(default=None, alias="AllDayAttendanceCode", description="The attendance code for the whole day. In a daily attendance school, this will be the only attendance code populated for the day. For a period attendance school, this should ordinarily be populated only if all period attendance codes are the same.")
    calendar_date: str | None = Field(default=None, alias="CalendarDate", description="The calendar date for this attendance")
    attendance_code: int | str | None = Field(default=None, alias="AttendanceCode", description="For Traditional Schools, the Code will come from ATT. For Flex Schools it will use CAT.")
    section_number: int | str | None = Field(default=None, alias="SectionNumber", description="For Flex Schools the section will come form the CAT table For Traditional Schools it will come from CAR")
    period: str | None = Field(default=None, alias="Period", description="For Traditional Schools, Period will still come from ATT For Flex Schools it will use FTF")

class AttendanceGetAttendanceHistorySummaryResponse(AeriesModel):
    """Response model for `attendance.get_attendance_history_summary`."""
    days_absence: int | str | None = Field(default=None, alias="DaysAbsence", description="The total number of days (according to the All Day attendance code) of absence this student has in the given school year and school code")
    days_enrolled: int | str | None = Field(default=None, alias="DaysEnrolled", description="The total number of days (according to the All Day attendance code) of enrollment this student has in the given school year and school code")
    days_excused: int | str | None = Field(default=None, alias="DaysExcused", description="The total number of days (according to the All Day attendance code) of excused absence this student has in the given school year and school code")
    days_of_truancy: int | str | None = Field(default=None, alias="DaysOfTruancy", description="The total number of days the student has any truancy attendance code in the given school year and school code")
    days_present: int | str | None = Field(default=None, alias="DaysPresent", description="The total number of days (according to the All Day attendance code) present this student has in the given school year and school code")
    days_suspension: int | str | None = Field(default=None, alias="DaysSuspension", description="The total number of days (according to the All Day attendance code) of suspension this student has in the given school year and school code")
    days_tardy: int | str | None = Field(default=None, alias="DaysTardy", description="The total number of days (according to the All Day attendance code) tardy this student has in the given school year and school code")
    days_unexcused: int | str | None = Field(default=None, alias="DaysUnexcused", description="The total number of days (according to the All Day attendance code) of unexcused absence this student has in the given school year and school code")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    school_year: str | None = Field(default=None, alias="SchoolYear", description="The school year, in the format “yyyy-yyyy”; e.g., “2024-2025”")
    student_id: str | None = Field(default=None, alias="StudentID", description="The StudentID")
    attendance_program_code_primary: int | str | None = Field(default=None, alias="AttendanceProgramCodePrimary", description="Students' Primary Attendance Program")
    roporting_school_code: int | str | None = Field(default=None, alias="RoportingSchoolCode", description="Students' Reporting School")
    days_complete_independent_study: int | str | None = Field(default=None, alias="DaysCompleteIndependentStudy", description="Number of Days Student has Completed Independent Study work")
    days_incomplete_independent_study: int | str | None = Field(default=None, alias="DaysIncompleteIndependentStudy", description="Number of Days Student marked Incomplete for Independent Study work")
    days_in_school_suspension: int | str | None = Field(default=None, alias="DaysInSchoolSuspension", description="Number of Days Student has served In School Suspension")
    period_expected_to_attend: int | str | None = Field(default=None, alias="PeriodExpectedToAttend", description="For Hourly Attendance - Daily Number of Periods the Student is Expected to Attend")
    periods_attended: int | str | None = Field(default=None, alias="PeriodsAttended", description="For Hourly Attendance - Daily Number of Periods the Student Attended")
    periods_out_of_school_suspension: int | str | None = Field(default=None, alias="PeriodsOutOfSchoolSuspension", description="Daily Number of Periods the Student served Out of School Suspension")
    periods_attended_in_school_suspension: int | str | None = Field(default=None, alias="PeriodsAttendedInSchoolSuspension", description="Daily Number of Periods the Student served In School Suspension")
    periods_excused_absence: int | str | None = Field(default=None, alias="PeriodsExcusedAbsence", description="Daily Number of Periods the Student has an Excused Absence")
    periods_unexcused_absence: int | str | None = Field(default=None, alias="PeriodsUnexcusedAbsence", description="Daily Number of Periods the Student has an Unexcused Absence")
    periods_complete_independent_study: int | str | None = Field(default=None, alias="PeriodsCompleteIndependentStudy", description="Daily Number of Periods the Student Completed Independent Study work")
    periods_incomplete_independent_study: int | str | None = Field(default=None, alias="PeriodsIncompleteIndependentStudy", description="Daily Number of Periods Student marked Incomplete for Independent Study work")

class AttendanceGetAttendanceHistorySummaryYearYearResponse(AeriesModel):
    """Response model for `attendance.get_attendance_history_summary_year_year`."""
    days_absence: int | str | None = Field(default=None, alias="DaysAbsence", description="The total number of days (according to the All Day attendance code) of absence this student has in the given school year and school code")
    days_enrolled: int | str | None = Field(default=None, alias="DaysEnrolled", description="The total number of days (according to the All Day attendance code) of enrollment this student has in the given school year and school code")
    days_excused: int | str | None = Field(default=None, alias="DaysExcused", description="The total number of days (according to the All Day attendance code) of excused absence this student has in the given school year and school code")
    days_of_truancy: int | str | None = Field(default=None, alias="DaysOfTruancy", description="The total number of days the student has any truancy attendance code in the given school year and school code")
    days_present: int | str | None = Field(default=None, alias="DaysPresent", description="The total number of days (according to the All Day attendance code) present this student has in the given school year and school code")
    days_suspension: int | str | None = Field(default=None, alias="DaysSuspension", description="The total number of days (according to the All Day attendance code) of suspension this student has in the given school year and school code")
    days_tardy: int | str | None = Field(default=None, alias="DaysTardy", description="The total number of days (according to the All Day attendance code) tardy this student has in the given school year and school code")
    days_unexcused: int | str | None = Field(default=None, alias="DaysUnexcused", description="The total number of days (according to the All Day attendance code) of unexcused absence this student has in the given school year and school code")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    school_year: str | None = Field(default=None, alias="SchoolYear", description="The school year, in the format “yyyy-yyyy”; e.g., “2024-2025”")
    student_id: str | None = Field(default=None, alias="StudentID", description="The StudentID")
    attendance_program_code_primary: int | str | None = Field(default=None, alias="AttendanceProgramCodePrimary", description="Students' Primary Attendance Program")
    roporting_school_code: int | str | None = Field(default=None, alias="RoportingSchoolCode", description="Students' Reporting School")
    days_complete_independent_study: int | str | None = Field(default=None, alias="DaysCompleteIndependentStudy", description="Number of Days Student has Completed Independent Study work")
    days_incomplete_independent_study: int | str | None = Field(default=None, alias="DaysIncompleteIndependentStudy", description="Number of Days Student marked Incomplete for Independent Study work")
    days_in_school_suspension: int | str | None = Field(default=None, alias="DaysInSchoolSuspension", description="Number of Days Student has served In School Suspension")
    period_expected_to_attend: int | str | None = Field(default=None, alias="PeriodExpectedToAttend", description="For Hourly Attendance - Daily Number of Periods the Student is Expected to Attend")
    periods_attended: int | str | None = Field(default=None, alias="PeriodsAttended", description="For Hourly Attendance - Daily Number of Periods the Student Attended")
    periods_out_of_school_suspension: int | str | None = Field(default=None, alias="PeriodsOutOfSchoolSuspension", description="Daily Number of Periods the Student served Out of School Suspension")
    periods_attended_in_school_suspension: int | str | None = Field(default=None, alias="PeriodsAttendedInSchoolSuspension", description="Daily Number of Periods the Student served In School Suspension")
    periods_excused_absence: int | str | None = Field(default=None, alias="PeriodsExcusedAbsence", description="Daily Number of Periods the Student has an Excused Absence")
    periods_unexcused_absence: int | str | None = Field(default=None, alias="PeriodsUnexcusedAbsence", description="Daily Number of Periods the Student has an Unexcused Absence")
    periods_complete_independent_study: int | str | None = Field(default=None, alias="PeriodsCompleteIndependentStudy", description="Daily Number of Periods the Student Completed Independent Study work")
    periods_incomplete_independent_study: int | str | None = Field(default=None, alias="PeriodsIncompleteIndependentStudy", description="Daily Number of Periods Student marked Incomplete for Independent Study work")

class AttendanceGetAttendanceHistoryDetailsResponse(AeriesModel):
    """Response model for `attendance.get_attendance_history_details`."""
    pass

class AttendanceGetAttendanceHistoryDetailsYearYearResponse(AeriesModel):
    """Response model for `attendance.get_attendance_history_details_year_year`."""
    pass

class AttendanceGetAttendanceHistoryAttendanceCodesResponse(AeriesModel):
    """Response model for `attendance.get_attendance_history_attendance_codes`."""
    abbreviation: int | str | None = Field(default=None, alias="Abbreviation", description="The abbreviated name (max 3 characters) for this absence code")
    absence_code: int | str | None = Field(default=None, alias="AbsenceCode", description="The absence code (1 character). This will typically be a letter A-Z but may be a digit.")
    count_on_report_card: int | str | None = Field(default=None, alias="CountOnReportCard", description="Indicates whether this absence code counts toward attendance totals on the grade report card.")
    counts_for_ada: int | str | None = Field(default=None, alias="CountsForADA", description="Indicates whether this absence code counts toward the school’s ADA apportionment calculation.")
    include_in_parent_notifications: int | str | None = Field(default=None, alias="IncludeInParentNotifications", description="Indicates whether this absence code should be included when notifications are sent to parents (e.g., automated attendance calls).")
    include_on_letters: int | str | None = Field(default=None, alias="IncludeOnLetters", description="Indicates whether this absence code should be included on letters sent to parents")
    include_on_reports: int | str | None = Field(default=None, alias="IncludeOnReports", description="Indicates whether this absence code should print on attendance reports.")
    is_partial_day_truant: int | str | None = Field(default=None, alias="IsPartialDayTruant", description="Indicates whether this absence code represents a partial day truancy. It would normally be used for a student who is more than 30 minutes late for class.")
    is_suspension: int | str | None = Field(default=None, alias="IsSuspension", description="Indicates whether this absence code represents a suspension (may be in-school or out-of-school).")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    school_year: str | None = Field(default=None, alias="SchoolYear", description="The school year to which this record applies")
    title: int | str | None = Field(default=None, alias="Title", description="The full name (max 10 characters) for this absence code")
    type: int | str | None = Field(default=None, alias="Type", description="A code representing the type of absence code.")
    is_temporarily_not_enrolled: int | str | None = Field(default=None, alias="IsTemporarilyNotEnrolled", description="Absence Code will count the Student as Not Enrolled for this day")
    independent_study_code: int | str | None = Field(default=None, alias="IndependentStudyCode", description="Absence code applies to Independent Study Students")

class AttendanceGetAttendanceHistoryAttendanceCodesYearYearResponse(AeriesModel):
    """Response model for `attendance.get_attendance_history_attendance_codes_year_year`."""
    abbreviation: int | str | None = Field(default=None, alias="Abbreviation", description="The abbreviated name (max 3 characters) for this absence code")
    absence_code: int | str | None = Field(default=None, alias="AbsenceCode", description="The absence code (1 character). This will typically be a letter A-Z but may be a digit.")
    count_on_report_card: int | str | None = Field(default=None, alias="CountOnReportCard", description="Indicates whether this absence code counts toward attendance totals on the grade report card.")
    counts_for_ada: int | str | None = Field(default=None, alias="CountsForADA", description="Indicates whether this absence code counts toward the school’s ADA apportionment calculation.")
    include_in_parent_notifications: int | str | None = Field(default=None, alias="IncludeInParentNotifications", description="Indicates whether this absence code should be included when notifications are sent to parents (e.g., automated attendance calls).")
    include_on_letters: int | str | None = Field(default=None, alias="IncludeOnLetters", description="Indicates whether this absence code should be included on letters sent to parents")
    include_on_reports: int | str | None = Field(default=None, alias="IncludeOnReports", description="Indicates whether this absence code should print on attendance reports.")
    is_partial_day_truant: int | str | None = Field(default=None, alias="IsPartialDayTruant", description="Indicates whether this absence code represents a partial day truancy. It would normally be used for a student who is more than 30 minutes late for class.")
    is_suspension: int | str | None = Field(default=None, alias="IsSuspension", description="Indicates whether this absence code represents a suspension (may be in-school or out-of-school).")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    school_year: str | None = Field(default=None, alias="SchoolYear", description="The school year to which this record applies")
    title: int | str | None = Field(default=None, alias="Title", description="The full name (max 10 characters) for this absence code")
    type: int | str | None = Field(default=None, alias="Type", description="A code representing the type of absence code.")
    is_temporarily_not_enrolled: int | str | None = Field(default=None, alias="IsTemporarilyNotEnrolled", description="Absence Code will count the Student as Not Enrolled for this day")
    independent_study_code: int | str | None = Field(default=None, alias="IndependentStudyCode", description="Absence code applies to Independent Study Students")

class StaffGetStaffInformationResponse(AeriesModel):
    """Response model for `staff.get_staff_information`."""
    alternate_email_address: str | None = Field(default=None, alias="AlternateEmailAddress", description="An alternate email address.")
    birth_date: str | None = Field(default=None, alias="BirthDate", description="Date of Birth")
    birth_year: str | None = Field(default=None, alias="BirthYear", description="(obsolete) Year of birth")
    cell_phone: int | str | None = Field(default=None, alias="CellPhone", description="Mobile phone number")
    email_address: str | None = Field(default=None, alias="EmailAddress", description="The staff member’s email address. (Will pull from STF.EM if UGN.EM is blank)")
    first_name: str | None = Field(default=None, alias="FirstName", description="The staff member’s first name")
    full_time_percentage: str | None = Field(default=None, alias="FullTimePercentage", description="The staff member’s full-time employment percentage")
    hire_date: str | None = Field(default=None, alias="HireDate", description="The staff member’s hire date")
    human_resources_system_id: str | None = Field(default=None, alias="HumanResourcesSystemID", description="An identifier for the staff member in an external Human Resources management system. While Aeries staff IDs are numeric, this field accepts all text characters.")
    id: str | None = Field(default=None, alias="ID", description="The Aeries District Staff ID")
    inactive_status_code: int | str | None = Field(default=None, alias="InactiveStatusCode", description="Any value other than blank indicates the staff member is inactive.")
    last_name: str | None = Field(default=None, alias="LastName", description="The staff member’s last name")
    leave_date: str | None = Field(default=None, alias="LeaveDate", description="The date the staff member’s employment terminated.")
    middle_name: str | None = Field(default=None, alias="MiddleName", description="The staff member’s middle name")
    network_login_id: int | str | None = Field(default=None, alias="NetworkLoginID", description="The staff member’s network login ID. This may be used by the district for any purpose they choose, such as an Active Directory account.")
    notification_preference_code: int | str | None = Field(default=None, alias="NotificationPreferenceCode", description="The staff member’s Aeries Comunications notification preference.")
    primary_aeries_school: int | str | None = Field(default=None, alias="PrimaryAeriesSchool", description="The Aeries school code of the school where the staff member is primarily employed.")
    communication_group: str | None = Field(default=None, alias="CommunicationGroup", description="Indicates whether the user should be included in school-wide communications for this school in the Aeries Communications system.")
    read_only_access: int | str | None = Field(default=None, alias="ReadOnlyAccess", description="Indicates whether this user has read-only access to the Aeries system for this school code. If True, the user is not permitted to make ANY changes to data when logged-in to this school code.")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code to which this user has access.")
    gender: str | None = Field(default=None, alias="Gender", description="The staff member’s sex (M or F)")
    state_educator_id: str | None = Field(default=None, alias="StateEducatorID", description="For certificated employees, the Statewide Educator ID issued by the state authority.")
    title: str | None = Field(default=None, alias="Title", description="The staff member’s title.")
    user_name: str | None = Field(default=None, alias="UserName", description="The staff member’s username for the Aeries SIS.")
    early_childhood_certification_code: int | str | None = Field(default=None, alias="EarlyChildhoodCertificationCode", description="Early Childhood Certification Code")
    monthly_minutes: str | None = Field(default=None, alias="MonthlyMinutes", description="Monthly Minutes")
    population_served_code: int | str | None = Field(default=None, alias="PopulationServedCode", description="Population Served Code")
    service_id_code: int | str | None = Field(default=None, alias="ServiceIdCode", description="Service ID Code")

class StaffCreateStaffInformationCreateResponse(AeriesModel):
    """Response model for `staff.create_staff_information_create`."""
    pass

class StaffUpdateStaffInformationUpdateResponse(AeriesModel):
    """Response model for `staff.update_staff_information_update`."""
    pass

class SchedulingGetCourseInformationResponse(AeriesModel):
    """Response model for `scheduling.get_course_information`."""
    csf_course_list: str | None = Field(default=None, alias="CSFCourseList", description="The standardized list from the California Scholarship Federation to which this course belongs.")
    csu_rule_can_be_an_elective: bool | None = Field(default=None, alias="CSU_Rule_CanBeAnElective", description="If flagged with a ‘G’ this course can roll into CSU Electives when the assigned subject area is full.")
    csu_rule_honors_code: int | str | None = Field(default=None, alias="CSU_Rule_HonorsCode", description="If flagged with ‘H’ this course is counted as an honors course for purposes of CSU Eligibility.")
    csu_rule_validation_level_code: int | str | None = Field(default=None, alias="CSU_Rule_ValidationLevelCode", description="Course Validation Level is allowed by CSU for certain flexibilities when evaluating whether or not a student has completed a particular subject and gained requirements necessary to enter college.")
    csu_subject_area_code: int | str | None = Field(default=None, alias="CSU_SubjectAreaCode", description="The Subject Area that this course will count toward for completing the CSU entrance requirements.")
    college_prep_indicator_code: int | str | None = Field(default=None, alias="CollegePrepIndicatorCode", description="Indicates whether the course is counted as a college preparatory course.")
    content_description: str | None = Field(default=None, alias="ContentDescription", description="More detailed description of the course and/or the course content.")
    credit_default: int | str | None = Field(default=None, alias="CreditDefault", description="Default number of credits that a student will receive by passing this course")
    credit_max: str | None = Field(default=None, alias="CreditMax", description="Maximum Credit that a student can receive by taking this course multiple times.")
    department_code: int | str | None = Field(default=None, alias="DepartmentCode", description="The department code allows sorting reports by department, such as English.")
    high_grade: str | None = Field(default=None, alias="HighGrade", description="Highest grade level that would normally take this course. Used in Scheduling to prevent students outside the grade range from being scheduled into the class.")
    id: int | str | None = Field(default=None, alias="ID", description="Identification assigned to a course that can be up to 6 characters in length. The ID can contain letters and/or numbers, for example ENG123 but MUST not start with a space or special character, such as an asterisk *")
    inactive_status_code: int | str | None = Field(default=None, alias="InactiveStatusCode", description="Any non-blank value will inactivate the course and prevent sections from being added to the Master Schedule and Scheduling Master Schedule.")
    long_description: str | None = Field(default=None, alias="LongDescription", description="The long course title (max 30 characters)")
    low_grade: str | None = Field(default=None, alias="LowGrade", description="Lowest grade level that would normally take this course. Used in Scheduling to prevent students outside the Grade Range from being scheduled into the class.")
    non_academic_or_honors_code: int | str | None = Field(default=None, alias="NonAcademicOrHonorsCode", description="Indicates whether the course is a (N) Non Academic or (H) Honors.")
    notes: str | None = Field(default=None, alias="Notes", description="Free-text note about this course")
    physical_education_indicator: str | None = Field(default=None, alias="PhysicalEducationIndicator", description="Indicates whether this course is a physical education course. Primarily used to single out the PE teacher among all a student’s teachers for purposes of entering Physical Fitness Test data.")
    state_course_code: int | str | None = Field(default=None, alias="StateCourseCode", description="Specific code assigned to courses by the California Department of Education that corresponds to the content of the course.")
    subject_area1_code: int | str | None = Field(default=None, alias="SubjectArea1Code", description="The first Graduation Requirements subject area that this course satisfies. Code description can be found through the Graduation Requirements API")
    subject_area2_code: int | str | None = Field(default=None, alias="SubjectArea2Code", description="The second Graduation Requirements subject area that this course satisfies if all requirements have been met for the S1 subject area. Code description can be found through the Graduation Requirements API")
    subject_area3_code: int | str | None = Field(default=None, alias="SubjectArea3Code", description="The third Graduation Requirements subject area that this course satisfies if all requirements have been met for the S1 and S2 subject areas. Code description can be found through the Graduation Requirements API")
    teacher_aide_indicator: str | None = Field(default=None, alias="TeacherAideIndicator", description="Indicates whether the course is a Teacher Aide course. Many reports within Aeries give users the option to skip TA courses.")
    term_type_code: int | str | None = Field(default=None, alias="TermTypeCode", description="Indicates the length of a given course.")
    title: str | None = Field(default=None, alias="Title", description="The short course title (max 15 characters)")
    uc_rule_can_be_an_elective: bool | None = Field(default=None, alias="UC_Rule_CanBeAnElective", description="If flagged with a ‘G’ this course can roll into UC Electives when the assigned subject area is full.")
    uc_rule_honors_code: int | str | None = Field(default=None, alias="UC_Rule_HonorsCode", description="If flagged with ‘H’ this course is counted as an honors course for purposes of UC Eligibility.")
    uc_rule_validation_level_code: int | str | None = Field(default=None, alias="UC_Rule_ValidationLevelCode", description="Course Validation Level is allowed by UC for certain flexibilities when evaluating whether or not a student has completed a particular subject and gained requirements necessary to enter college.")
    uc_subject_area_code: int | str | None = Field(default=None, alias="UC_SubjectAreaCode", description="The Subject Area that this course will count toward for completing the UC entrance requirements.")
    vocational_education_subject_area_code: int | str | None = Field(default=None, alias="VocationalEducationSubjectAreaCode", description="Vocational Education Subject Area")
    vocational_education_course_level_code: int | str | None = Field(default=None, alias="VocationalEducationCourseLevelCode", description="Vocational Education Course Level")
    course_level_code: int | str | None = Field(default=None, alias="CourseLevelCode", description="Academic Level of the Course")
    course_type_code: int | str | None = Field(default=None, alias="CourseTypeCode", description="Course Type")
    next_course: str | None = Field(default=None, alias="NextCourse", description="The Next Course in a Multi-Course Sequence")
    term_sequence: str | None = Field(default=None, alias="TermSequence", description="The Term Sequence for a Multi-Course Sequence")
    year_sequence: str | None = Field(default=None, alias="YearSequence", description="The Year Sequence for a Multi-Course Sequence")
    traditional_gender: str | None = Field(default=None, alias="TraditionalGender", description="(California only) The Gender a CTE course is 'Traditionally' for. Used for Carl Perkins Reporting. Informational only.")
    nclb_bore_code: int | str | None = Field(default=None, alias="NCLBBoreCode", description="NCLB Bore Code")
    nclb_bore_area1_code: int | str | None = Field(default=None, alias="NCLBBoreArea1Code", description="NCLB Bore Area 1")
    nclb_bore_area2_code: int | str | None = Field(default=None, alias="NCLBBoreArea2Code", description="NCLB Bore Area 2")
    content_group_code: int | str | None = Field(default=None, alias="ContentGroupCode", description="The Course Content Group field is used to link courses together that have the same content.")
    nces_code: int | str | None = Field(default=None, alias="NCESCode", description="This field is used to classify the content of the course for the National Center for Education Statistics.")
    cip_code: int | str | None = Field(default=None, alias="CIPCode", description="Classification of Instructional Programs code from the National Center for Education Statistics for use with adult education courses")
    board_adoption_date: str | None = Field(default=None, alias="BoardAdoptionDate", description="The date the course was adopted (approved) by the District Board of Education.")
    last_revision_date: str | None = Field(default=None, alias="LastRevisionDate", description="The date the framework of the course was last revised")
    revision_type_code: int | str | None = Field(default=None, alias="RevisionTypeCode", description="The type of revision that was made when the course framework was last revised.")
    inactive_date: str | None = Field(default=None, alias="InactiveDate", description="Date the Course was Inactivated")
    academic_weight: str | None = Field(default=None, alias="AcademicWeight", description="The Academic Weight field is available for use in 4 x 4 Block Scheduling. Valid values are 0-4. By assigning a value to each course the scheduler will attempt to balance the student’s work load for each semester.")
    meets_algebra_requirement: int | str | None = Field(default=None, alias="MeetsAlgebraRequirement", description="Indicates that this course will count towards the Algebra I requirement set by the State")
    algebra_i_credit_required: int | str | None = Field(default=None, alias="AlgebraICreditRequired", description="The number of credits required to meet the Algebra I requirement.")
    service_id: str | None = Field(default=None, alias="ServiceID", description="Service ID")
    population_served_code: int | str | None = Field(default=None, alias="PopulationServedCode", description="Population Served")
    class_type_code: int | str | None = Field(default=None, alias="ClassTypeCode", description="Class Type")
    course_sequence_code: int | str | None = Field(default=None, alias="CourseSequenceCode", description="Course Sequence")
    non_campus_based_instruction_code: int | str | None = Field(default=None, alias="NonCampusBasedInstructionCode", description="Non Campus Based Instruction Indicator")
    on_ramps_dual_enrollment_indicator: str | None = Field(default=None, alias="OnRampsDualEnrollmentIndicator", description="OnRamps Dual Enrollment Indicator")
    include_for_extracurricular_activity_eligibility_indicator: str | None = Field(default=None, alias="IncludeForExtracurricularActivityEligibilityIndicator", description="Included in Extracurricular Activity Eligibility status")
    content_subcategory_code: int | str | None = Field(default=None, alias="ContentSubcategoryCode", description="Content Subcategory")
    standards_grade_range_code: int | str | None = Field(default=None, alias="StandardsGradeRangeCode", description="Standard Grade Range")
    content_standards_alignment_code: int | str | None = Field(default=None, alias="ContentStandardsAlignmentCode", description="Content Standards Alignment")
    charter_non_core_indicator: str | None = Field(default=None, alias="CharterNonCoreIndicator", description="Charter NonCore Indicator")
    advanced_course_state_code: int | str | None = Field(default=None, alias="AdvancedCourseStateCode", description="Advanced Course State code")
    college_state_course_code: int | str | None = Field(default=None, alias="CollegeStateCourseCode", description="College State Course code")
    middle_school_core_indicator: str | None = Field(default=None, alias="MiddleSchoolCoreIndicator", description="Middle School Core Indicator")
    hours_for_completion: str | None = Field(default=None, alias="HoursForCompletion", description="Hours for Completion")
    cost_of_course: str | None = Field(default=None, alias="CostOfCourse", description="Cost of Course")
    correspondence_language_code1: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode1", description="Language Code of Translation")
    title_for_language1: str | None = Field(default=None, alias="TitleForLanguage1", description="Name of Language")
    correspondence_language_code2: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode2", description="Language Code of Translation")
    title_for_language2: str | None = Field(default=None, alias="TitleForLanguage2", description="Name of Language")
    correspondence_language_code3: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode3", description="Language Code of Translation")
    title_for_language3: str | None = Field(default=None, alias="TitleForLanguage3", description="Name of Language")
    correspondence_language_code4: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode4", description="Language Code of Translation")
    title_for_language4: str | None = Field(default=None, alias="TitleForLanguage4", description="Name of Language")
    correspondence_language_code5: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode5", description="Language Code of Translation")
    title_for_language5: str | None = Field(default=None, alias="TitleForLanguage5", description="Name of Language")
    correspondence_language_code6: int | str | None = Field(default=None, alias="CorrespondenceLanguageCode6", description="Language Code of Translation")
    title_for_language6: str | None = Field(default=None, alias="TitleForLanguage6", description="Name of Language")
    user_code1: int | str | None = Field(default=None, alias="UserCode1", description="User Code 1")
    user_code2: int | str | None = Field(default=None, alias="UserCode2", description="User Code 2")
    user_code3: int | str | None = Field(default=None, alias="UserCode3", description="User Code 3")
    user_code4: int | str | None = Field(default=None, alias="UserCode4", description="User Code 4")
    user_code5: int | str | None = Field(default=None, alias="UserCode5", description="User Code 5")
    user_code6: int | str | None = Field(default=None, alias="UserCode6", description="User Code 6")
    user_code7: int | str | None = Field(default=None, alias="UserCode7", description="User Code 7")
    user_code8: int | str | None = Field(default=None, alias="UserCode8", description="User Code 8")

class SchedulingGetCourseDataChangesResponse(AeriesModel):
    """Response model for `scheduling.get_course_data_changes`."""
    pass

class SchedulingGetSectionsFromMasterScheduleResponse(AeriesModel):
    """Response model for `scheduling.get_sections_from_master_schedule`."""
    pass

class SchedulingGetSectionDataChangesFromMasterScheduleResponse(AeriesModel):
    """Response model for `scheduling.get_section_data_changes_from_master_schedule`."""
    pass

class SchedulingGetStaffClassesSectionsResponse(AeriesModel):
    """Response model for `scheduling.get_staff_classes_sections`."""
    pass

class SchedulingGetSectionClassRosterResponse(AeriesModel):
    """Response model for `scheduling.get_section_class_roster`."""
    pass

class SchedulingGetSectionClassRosterDataChangesResponse(AeriesModel):
    """Response model for `scheduling.get_section_class_roster_data_changes`."""
    pass

class SchedulingGetSectionFromSchedulingMasterScheduleResponse(AeriesModel):
    """Response model for `scheduling.get_section_from_scheduling_master_schedule`."""
    pass

class SchedulingCreateSectionFromSchedulingMasterScheduleResponse(AeriesModel):
    """Response model for `scheduling.create_section_from_scheduling_master_schedule`."""
    pass

class GradebookGetGradebookInformationResponse(AeriesModel):
    """Response model for `gradebook.get_gradebook_information`."""
    comment: str | None = Field(default=None, alias="Comment", description="A comment associated with the gradebook for reference by the teacher.")
    end_date: str | None = Field(default=None, alias="EndDate", description="The ending date of the gradebook. Usually the last day of the term associated with the gradebook.")
    gradebook_number: str | None = Field(default=None, alias="GradebookNumber", description="The specific Aeries Gradebook Number. This is a unique number that is assigned at the time the gradebook is created and should not change.")
    gradebook_type: str | None = Field(default=None, alias="GradebookType", description="(not currently used)")
    linked_group: int | str | None = Field(default=None, alias="LinkedGroup", description="Linked Gradebooks group number. Gradebooks with the same number are considered linked together. A value of 0 is considered Ungrouped.")
    name: str | None = Field(default=None, alias="Name", description="The name of the gradebook as displayed throughout the system. This is typically the Course name; however, the teacher can modify the name.")
    period: str | None = Field(default=None, alias="Period", description="The period associated with this gradebook.")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    start_date: str | None = Field(default=None, alias="StartDate", description="The starting date of the gradebook. Usually the first day of the term associated with the gradebook.")
    teacher_email_address: str | None = Field(default=None, alias="TeacherEmailAddress", description="The teacher’s email address")
    teacher_name: str | None = Field(default=None, alias="TeacherName", description="The display name of the teacher. It may be different than teacher’s actual first and last name.")
    teacher_number: int | str | None = Field(default=None, alias="TeacherNumber", description="The school-based Aeries teacher number")

class GradebookGetGradebookInformationSchoolsSchoolCodeSectionsSectionNumberGradebooksResponse(AeriesModel):
    """Response model for `gradebook.get_gradebook_information_schools_school_code_sections_section_number_gradebooks`."""
    comment: str | None = Field(default=None, alias="Comment", description="A comment associated with the gradebook for reference by the teacher.")
    end_date: str | None = Field(default=None, alias="EndDate", description="The ending date of the gradebook. Usually the last day of the term associated with the gradebook.")
    gradebook_number: str | None = Field(default=None, alias="GradebookNumber", description="The specific Aeries Gradebook Number. This is a unique number that is assigned at the time the gradebook is created and should not change.")
    gradebook_type: str | None = Field(default=None, alias="GradebookType", description="(not currently used)")
    linked_group: int | str | None = Field(default=None, alias="LinkedGroup", description="Linked Gradebooks group number. Gradebooks with the same number are considered linked together. A value of 0 is considered Ungrouped.")
    name: str | None = Field(default=None, alias="Name", description="The name of the gradebook as displayed throughout the system. This is typically the Course name; however, the teacher can modify the name.")
    period: str | None = Field(default=None, alias="Period", description="The period associated with this gradebook.")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    start_date: str | None = Field(default=None, alias="StartDate", description="The starting date of the gradebook. Usually the first day of the term associated with the gradebook.")
    teacher_email_address: str | None = Field(default=None, alias="TeacherEmailAddress", description="The teacher’s email address")
    teacher_name: str | None = Field(default=None, alias="TeacherName", description="The display name of the teacher. It may be different than teacher’s actual first and last name.")
    teacher_number: int | str | None = Field(default=None, alias="TeacherNumber", description="The school-based Aeries teacher number")

class GradebookGetGradebookInformationGradebooksGradebookNumberResponse(AeriesModel):
    """Response model for `gradebook.get_gradebook_information_gradebooks_gradebook_number`."""
    comment: str | None = Field(default=None, alias="Comment", description="A comment associated with the gradebook for reference by the teacher.")
    end_date: str | None = Field(default=None, alias="EndDate", description="The ending date of the gradebook. Usually the last day of the term associated with the gradebook.")
    gradebook_number: str | None = Field(default=None, alias="GradebookNumber", description="The specific Aeries Gradebook Number. This is a unique number that is assigned at the time the gradebook is created and should not change.")
    gradebook_type: str | None = Field(default=None, alias="GradebookType", description="(not currently used)")
    linked_group: int | str | None = Field(default=None, alias="LinkedGroup", description="Linked Gradebooks group number. Gradebooks with the same number are considered linked together. A value of 0 is considered Ungrouped.")
    name: str | None = Field(default=None, alias="Name", description="The name of the gradebook as displayed throughout the system. This is typically the Course name; however, the teacher can modify the name.")
    period: str | None = Field(default=None, alias="Period", description="The period associated with this gradebook.")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    start_date: str | None = Field(default=None, alias="StartDate", description="The starting date of the gradebook. Usually the first day of the term associated with the gradebook.")
    teacher_email_address: str | None = Field(default=None, alias="TeacherEmailAddress", description="The teacher’s email address")
    teacher_name: str | None = Field(default=None, alias="TeacherName", description="The display name of the teacher. It may be different than teacher’s actual first and last name.")
    teacher_number: int | str | None = Field(default=None, alias="TeacherNumber", description="The school-based Aeries teacher number")

class GradebookGetAssignmentInformationResponse(AeriesModel):
    """Response model for `gradebook.get_assignment_information`."""
    aeries_analytics_exam_id: str | None = Field(default=None, alias="AeriesAnalyticsExamID", description="(no longer used)")
    aeries_analytics_exam_test_admin: str | None = Field(default=None, alias="AeriesAnalyticsExamTestAdmin", description="(no longer used)")
    allow_student_drop_box: str | None = Field(default=None, alias="AllowStudentDropBox", description="If turned on, this allows students to upload a document to this particular assignment via the Aeries Student Portal.")
    assignment_number: int | str | None = Field(default=None, alias="AssignmentNumber", description="The specific Assignment Number")
    comment: str | None = Field(default=None, alias="Comment", description="This is a longer description of the assignment")
    date_assigned: str | None = Field(default=None, alias="DateAssigned", description="The date the assignment was assigned")
    date_due: str | None = Field(default=None, alias="DateDue", description="The date the assignment is due.")
    description: str | None = Field(default=None, alias="Description", description="The name of the assignment as displayed throughout the system")
    due_time: str | None = Field(default=None, alias="DueTime", description="Used in conjunction with the AllowStudentDropBox option. The document can only be uploaded until this time.")
    external_id: str | None = Field(default=None, alias="ExternalID", description="This is used to identify an assignment in third party systems such as Google Classroom.")
    formative_summative_indicator: str | None = Field(default=None, alias="FormativeSummativeIndicator", description="Defines an assignment as either Formative or Summative.")
    gradebook_number: int | str | None = Field(default=None, alias="GradebookNumber", description="The specific Aeries Gradebook Number")
    grading_completed: int | str | None = Field(default=None, alias="GradingCompleted", description="This is a flag that notes whether the teacher is finished grading this assignment. Once the flag is turned on, the scores count toward students’ overall grade and will be considered “missing” if not yet scored.")
    input_scores_by_standard: str | None = Field(default=None, alias="InputScoresByStandard", description="This denotes that the assignment is Input by Standard. Teachers will enter multiple scores per assignment, one for each standard.")
    narrative_grade_set_id: str | None = Field(default=None, alias="NarrativeGradeSetID", description="If a narrative grading scale is in use on this assignment, this denotes which one is being used. A narrative grade set allows the teacher to choose from a list of marks rather than enter a numeric score for each student. Each narrative grade mark then corresponds to a certain percentage correct.")
    number_correct_possible: int | str | None = Field(default=None, alias="NumberCorrectPossible", description="The number of questions (or points) possible for this assignment.")
    points_possible: int | str | None = Field(default=None, alias="PointsPossible", description="The maximum number of points that can be earned on this assignment.")
    rubric_assignment: str | None = Field(default=None, alias="RubricAssignment", description="Indicates whether this assignment is using Rubric Grading")
    scores_visible_to_parents: str | None = Field(default=None, alias="ScoresVisibleToParents", description="The score is visible to parents and students in the Aeries Parent/Student Portal. Parents may see the assignment but not the score.")
    unique_id: int | str | None = Field(default=None, alias="UniqueID", description="The District-wide Unique ID for this assignment. The teacher has the ability to change the Assignment Number, but the Unique ID for an assignment will never change. Once the Unique ID is known, it can be used to guarantee that future API calls refer to the same assignment.")
    visible_to_parents: bool | None = Field(default=None, alias="VisibleToParents", description="The assignment is visible to parents and students in the Aeries Parent/Student Portal. Neither the score nor the assignment will be shown if this is False.")

class GradebookGetAssignmentInformationAssignmentsUniqueIdResponse(AeriesModel):
    """Response model for `gradebook.get_assignment_information_assignments_unique_id`."""
    aeries_analytics_exam_id: str | None = Field(default=None, alias="AeriesAnalyticsExamID", description="(no longer used)")
    aeries_analytics_exam_test_admin: str | None = Field(default=None, alias="AeriesAnalyticsExamTestAdmin", description="(no longer used)")
    allow_student_drop_box: str | None = Field(default=None, alias="AllowStudentDropBox", description="If turned on, this allows students to upload a document to this particular assignment via the Aeries Student Portal.")
    assignment_number: int | str | None = Field(default=None, alias="AssignmentNumber", description="The specific Assignment Number")
    comment: str | None = Field(default=None, alias="Comment", description="This is a longer description of the assignment")
    date_assigned: str | None = Field(default=None, alias="DateAssigned", description="The date the assignment was assigned")
    date_due: str | None = Field(default=None, alias="DateDue", description="The date the assignment is due.")
    description: str | None = Field(default=None, alias="Description", description="The name of the assignment as displayed throughout the system")
    due_time: str | None = Field(default=None, alias="DueTime", description="Used in conjunction with the AllowStudentDropBox option. The document can only be uploaded until this time.")
    external_id: str | None = Field(default=None, alias="ExternalID", description="This is used to identify an assignment in third party systems such as Google Classroom.")
    formative_summative_indicator: str | None = Field(default=None, alias="FormativeSummativeIndicator", description="Defines an assignment as either Formative or Summative.")
    gradebook_number: int | str | None = Field(default=None, alias="GradebookNumber", description="The specific Aeries Gradebook Number")
    grading_completed: int | str | None = Field(default=None, alias="GradingCompleted", description="This is a flag that notes whether the teacher is finished grading this assignment. Once the flag is turned on, the scores count toward students’ overall grade and will be considered “missing” if not yet scored.")
    input_scores_by_standard: str | None = Field(default=None, alias="InputScoresByStandard", description="This denotes that the assignment is Input by Standard. Teachers will enter multiple scores per assignment, one for each standard.")
    narrative_grade_set_id: str | None = Field(default=None, alias="NarrativeGradeSetID", description="If a narrative grading scale is in use on this assignment, this denotes which one is being used. A narrative grade set allows the teacher to choose from a list of marks rather than enter a numeric score for each student. Each narrative grade mark then corresponds to a certain percentage correct.")
    number_correct_possible: int | str | None = Field(default=None, alias="NumberCorrectPossible", description="The number of questions (or points) possible for this assignment.")
    points_possible: int | str | None = Field(default=None, alias="PointsPossible", description="The maximum number of points that can be earned on this assignment.")
    rubric_assignment: str | None = Field(default=None, alias="RubricAssignment", description="Indicates whether this assignment is using Rubric Grading")
    scores_visible_to_parents: str | None = Field(default=None, alias="ScoresVisibleToParents", description="The score is visible to parents and students in the Aeries Parent/Student Portal. Parents may see the assignment but not the score.")
    unique_id: int | str | None = Field(default=None, alias="UniqueID", description="The District-wide Unique ID for this assignment. The teacher has the ability to change the Assignment Number, but the Unique ID for an assignment will never change. Once the Unique ID is known, it can be used to guarantee that future API calls refer to the same assignment.")
    visible_to_parents: bool | None = Field(default=None, alias="VisibleToParents", description="The assignment is visible to parents and students in the Aeries Parent/Student Portal. Neither the score nor the assignment will be shown if this is False.")

class GradebookUpdateUpdatingAssignmentInformationResponse(AeriesModel):
    """Response model for `gradebook.update_updating_assignment_information`."""
    pass

class GradebookUpdateUpdatingAssignmentInformationAssignmentsUniqueIdResponse(AeriesModel):
    """Response model for `gradebook.update_updating_assignment_information_assignments_unique_id`."""
    pass

class GradebookCreateInsertingANewAssignmentResponse(AeriesModel):
    """Response model for `gradebook.create_inserting_a_new_assignment`."""
    pass

class GradebookGetFinalMarkRangesResponse(AeriesModel):
    """Response model for `gradebook.get_final_mark_ranges`."""
    high_value: str | None = Field(default=None, alias="HighValue", description="High Value (informational only see note above)")
    low_value: str | None = Field(default=None, alias="LowValue", description="The Low Value for this range.")
    mark: str | None = Field(default=None, alias="Mark", description="The Mark assigned to this range ex. A, B+, etc.")

class GradebookGetGradebookStudentInformationResponse(AeriesModel):
    """Response model for `gradebook.get_gradebook_student_information`."""
    current_mark: str | None = Field(default=None, alias="CurrentMark", description="The student’s overall current mark for this gradebook.")
    current_percentage: str | None = Field(default=None, alias="CurrentPercentage", description="The student’s overall current percentage for this gradebook.")
    current_term: str | None = Field(default=None, alias="CurrentTerm", description="The term that this mark applies to. Usually F, S, Y, 1, 2, 3, or 4.")
    custom_sort_order: str | None = Field(default=None, alias="CustomSortOrder", description="A custom sort order that a teacher can assign to sort students in their gradebook.")
    end_date: str | None = Field(default=None, alias="EndDate", description="The student’s end date for this gradebook. Normally the last day of the term unless the student dropped the class at an earlier date.")
    high_assignment_number: int | str | None = Field(default=None, alias="HighAssignmentNumber", description="(no longer used)")
    inactive_tag: str | None = Field(default=None, alias="InactiveTag", description="Is the student inactive in this gradebook")
    low_assignment_number: int | str | None = Field(default=None, alias="LowAssignmentNumber", description="(no longer used)")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Permanent ID of this student")
    school_code: int | str | None = Field(default=None, alias="SchoolCode", description="The Aeries school code")
    start_date: str | None = Field(default=None, alias="StartDate", description="The student’s beginning date for this gradebook. Normally the first day of the term unless the student enrolled in the class at a later date.")
    student_first_name: str | None = Field(default=None, alias="StudentFirstName", description="The student’s first name")
    student_grade_level: str | None = Field(default=None, alias="StudentGradeLevel", description="The student’s grade level")
    student_last_name: str | None = Field(default=None, alias="StudentLastName", description="The student’s last name")
    student_middle_name: str | None = Field(default=None, alias="StudentMiddleName", description="The student’s middle name")
    student_number: int | str | None = Field(default=None, alias="StudentNumber", description="The school-based Student Number for this student")
    student_sex: int | str | None = Field(default=None, alias="StudentSex", description="The student's sex or gender (May be M or F or another coded value for non-binary gender identifications)")

class GradebookGetAssignmentScoresResponse(AeriesModel):
    """Response model for `gradebook.get_assignment_scores`."""
    assignment_number: int | str | None = Field(default=None, alias="AssignmentNumber", description="The specific Assignment Number")
    date_completed: str | None = Field(default=None, alias="DateCompleted", description="The date the student completed/submitted the assignment")
    gradebook_number: int | str | None = Field(default=None, alias="GradebookNumber", description="The specific Aeries Gradebook Number")
    is_missing: int | str | None = Field(default=None, alias="IsMissing", description="Indicates whether this counts as a missing assignment for the student. Typically, this will be true under the following conditions: The student is not permanently excused from the assignment The student has no mark entered on the assignment The Grading Completed flag for the assignment is set to true")
    is_rule_replacing_score: str | None = Field(default=None, alias="IsRuleReplacingScore", description="Indicates whether a Gradebook Rule will replace this student’s actual score in the overall grade calculation. Gradebook Rules can be set by the teacher for each Gradebook. For example: drop the lowest score in the Quiz category and replace it with the average of remaining scores in the Quiz category.")
    mark: str | None = Field(default=None, alias="Mark", description="The mark entered for the student on this assignment. Usually numeric, but there are special marks such as “NA” (not applicable; i.e., excused) and “TX” (temporarily excused). Also, if a Narrative Grade set is used, the mark from the Narrative Grade set will display here. Also, marks can be expressed as a percentage such as 95%.")
    number_correct: int | str | None = Field(default=None, alias="NumberCorrect", description="The number of questions (or points) the student answered correctly.")
    number_correct_possible: int | str | None = Field(default=None, alias="NumberCorrectPossible", description="The number of questions (or points) possible for this assignment for this student.")
    percent_correct: str | None = Field(default=None, alias="PercentCorrect", description="The percentage of possible points earned by the student.")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Permanent ID of the student")
    points_earned: int | str | None = Field(default=None, alias="PointsEarned", description="The number of points earned by the student")
    points_possible: int | str | None = Field(default=None, alias="PointsPossible", description="The maximum number of points the student could have earned")
    rule_number_applied: int | str | None = Field(default=None, alias="RuleNumberApplied", description="If a Gradebook Rule was applied to this score, this is the rule number. Note: There is currently no API end point that provides detailed information on Gradebook Rules")
    rule_replaced_score: str | None = Field(default=None, alias="RuleReplacedScore", description="The percent score that will replace this student’s actual score due to a Gradebook Rule being applied. Expressed as a decimal (e.g., 0.9 = 90%)")

class GradebookGetAssignmentScoresAssignmentsUniqueIdScoresStudentIdResponse(AeriesModel):
    """Response model for `gradebook.get_assignment_scores_assignments_unique_id_scores_student_id`."""
    assignment_number: int | str | None = Field(default=None, alias="AssignmentNumber", description="The specific Assignment Number")
    date_completed: str | None = Field(default=None, alias="DateCompleted", description="The date the student completed/submitted the assignment")
    gradebook_number: int | str | None = Field(default=None, alias="GradebookNumber", description="The specific Aeries Gradebook Number")
    is_missing: int | str | None = Field(default=None, alias="IsMissing", description="Indicates whether this counts as a missing assignment for the student. Typically, this will be true under the following conditions: The student is not permanently excused from the assignment The student has no mark entered on the assignment The Grading Completed flag for the assignment is set to true")
    is_rule_replacing_score: str | None = Field(default=None, alias="IsRuleReplacingScore", description="Indicates whether a Gradebook Rule will replace this student’s actual score in the overall grade calculation. Gradebook Rules can be set by the teacher for each Gradebook. For example: drop the lowest score in the Quiz category and replace it with the average of remaining scores in the Quiz category.")
    mark: str | None = Field(default=None, alias="Mark", description="The mark entered for the student on this assignment. Usually numeric, but there are special marks such as “NA” (not applicable; i.e., excused) and “TX” (temporarily excused). Also, if a Narrative Grade set is used, the mark from the Narrative Grade set will display here. Also, marks can be expressed as a percentage such as 95%.")
    number_correct: int | str | None = Field(default=None, alias="NumberCorrect", description="The number of questions (or points) the student answered correctly.")
    number_correct_possible: int | str | None = Field(default=None, alias="NumberCorrectPossible", description="The number of questions (or points) possible for this assignment for this student.")
    percent_correct: str | None = Field(default=None, alias="PercentCorrect", description="The percentage of possible points earned by the student.")
    student_id: str | None = Field(default=None, alias="StudentID", description="The Permanent ID of the student")
    points_earned: int | str | None = Field(default=None, alias="PointsEarned", description="The number of points earned by the student")
    points_possible: int | str | None = Field(default=None, alias="PointsPossible", description="The maximum number of points the student could have earned")
    rule_number_applied: int | str | None = Field(default=None, alias="RuleNumberApplied", description="If a Gradebook Rule was applied to this score, this is the rule number. Note: There is currently no API end point that provides detailed information on Gradebook Rules")
    rule_replaced_score: str | None = Field(default=None, alias="RuleReplacedScore", description="The percent score that will replace this student’s actual score due to a Gradebook Rule being applied. Expressed as a decimal (e.g., 0.9 = 90%)")

class GradebookCreateUpdatingAssignmentScoresResponse(AeriesModel):
    """Response model for `gradebook.create_updating_assignment_scores`."""
    pass

class GradebookCreateUpdatingAssignmentScoresAssignmentsUniqueIdScoresResponse(AeriesModel):
    """Response model for `gradebook.create_updating_assignment_scores_assignments_unique_id_scores`."""
    pass

MODEL_REGISTRY: dict[str, type[AeriesModel]] = {
    "SchoolsGetAeriesInstallationInformationResponse": SchoolsGetAeriesInstallationInformationResponse,
    "SchoolsGetSchoolInformationResponse": SchoolsGetSchoolInformationResponse,
    "SchoolsGetSchoolTermsResponse": SchoolsGetSchoolTermsResponse,
    "SchoolsGetSchoolCalendarResponse": SchoolsGetSchoolCalendarResponse,
    "SchoolsGetBellScheduleResponse": SchoolsGetBellScheduleResponse,
    "SchoolsGetBellScheduleDateDateResponse": SchoolsGetBellScheduleDateDateResponse,
    "SchoolsGetAbsenceCodesResponse": SchoolsGetAbsenceCodesResponse,
    "SchoolsGetCodeSetsResponse": SchoolsGetCodeSetsResponse,
    "PreEnrollmentPreEnrollStudentResponse": PreEnrollmentPreEnrollStudentResponse,
    "PreEnrollmentPreEnrollInactiveStudentResponse": PreEnrollmentPreEnrollInactiveStudentResponse,
    "StudentsGetStudentInformationResponse": StudentsGetStudentInformationResponse,
    "StudentsGetStudentInformationGradeGradeLevelResponse": StudentsGetStudentInformationGradeGradeLevelResponse,
    "StudentsGetStudentInformationSnStudentNumberResponse": StudentsGetStudentInformationSnStudentNumberResponse,
    "StudentsCreateStudentInformationCreateResponse": StudentsCreateStudentInformationCreateResponse,
    "StudentsCreateStudentInformationUpdateResponse": StudentsCreateStudentInformationUpdateResponse,
    "StudentsCreateUpdateAddressResponse": StudentsCreateUpdateAddressResponse,
    "StudentsGetStudentInformationExtendedResponse": StudentsGetStudentInformationExtendedResponse,
    "StudentsGetStudentInformationExtendedGradeGradeLevelExtendedResponse": StudentsGetStudentInformationExtendedGradeGradeLevelExtendedResponse,
    "StudentsGetStudentInformationExtendedSnStudentNumberExtendedResponse": StudentsGetStudentInformationExtendedSnStudentNumberExtendedResponse,
    "StudentsGetStudentDataChangesResponse": StudentsGetStudentDataChangesResponse,
    "StudentsGetContactsResponse": StudentsGetContactsResponse,
    "StudentsCreateContactsCreateResponse": StudentsCreateContactsCreateResponse,
    "StudentsGetProgramsResponse": StudentsGetProgramsResponse,
    "StudentsGetTestScoresResponse": StudentsGetTestScoresResponse,
    "StudentsGetUpdateTestScoresResponse": StudentsGetUpdateTestScoresResponse,
    "StudentsGetCollegeEntranceTestScoresResponse": StudentsGetCollegeEntranceTestScoresResponse,
    "StudentsGetAssertiveDisciplineResponse": StudentsGetAssertiveDisciplineResponse,
    "StudentsGetDisciplineResponse": StudentsGetDisciplineResponse,
    "StudentsGetDistrictSupplementalStudentDataResponse": StudentsGetDistrictSupplementalStudentDataResponse,
    "StudentsGetSchoolSupplementalStudentDataResponse": StudentsGetSchoolSupplementalStudentDataResponse,
    "StudentsGetFeesAndFinesResponse": StudentsGetFeesAndFinesResponse,
    "StudentsGetStudentPictureResponse": StudentsGetStudentPictureResponse,
    "StudentsGetStudentGroupsResponse": StudentsGetStudentGroupsResponse,
    "GradesGetStudentGpAsResponse": GradesGetStudentGpAsResponse,
    "GradesGetStudentGradesResponse": GradesGetStudentGradesResponse,
    "GradesGetStudentReportCardsResponse": GradesGetStudentReportCardsResponse,
    "GradesGetSchoolReportCardMarkingPeriodsResponse": GradesGetSchoolReportCardMarkingPeriodsResponse,
    "GradesGetSchoolGraduationRequirementsResponse": GradesGetSchoolGraduationRequirementsResponse,
    "GradesGetStudentGraduationStatusSummaryResponse": GradesGetStudentGraduationStatusSummaryResponse,
    "GradesGetStudentGraduationStatusSummaryGradeGradeLevelResponse": GradesGetStudentGraduationStatusSummaryGradeGradeLevelResponse,
    "GradesGetStudentTranscriptsResponse": GradesGetStudentTranscriptsResponse,
    "GradesGetValidMarksResponse": GradesGetValidMarksResponse,
    "AttendanceGetStudentEnrollmentHistoryResponse": AttendanceGetStudentEnrollmentHistoryResponse,
    "AttendanceGetStudentEnrollmentHistoryYearAcademicYearResponse": AttendanceGetStudentEnrollmentHistoryYearAcademicYearResponse,
    "AttendanceGetStudentEnrollmentHistorySchoolsSchoolCodeEnrollmentStudentIdResponse": AttendanceGetStudentEnrollmentHistorySchoolsSchoolCodeEnrollmentStudentIdResponse,
    "AttendanceGetStudentEnrollmentHistorySchoolsSchoolCodeEnrollmentStudentIdYearAcademicYearResponse": AttendanceGetStudentEnrollmentHistorySchoolsSchoolCodeEnrollmentStudentIdYearAcademicYearResponse,
    "AttendanceGetStudentAttendanceResponse": AttendanceGetStudentAttendanceResponse,
    "AttendanceGetAttendanceHistorySummaryResponse": AttendanceGetAttendanceHistorySummaryResponse,
    "AttendanceGetAttendanceHistorySummaryYearYearResponse": AttendanceGetAttendanceHistorySummaryYearYearResponse,
    "AttendanceGetAttendanceHistoryDetailsResponse": AttendanceGetAttendanceHistoryDetailsResponse,
    "AttendanceGetAttendanceHistoryDetailsYearYearResponse": AttendanceGetAttendanceHistoryDetailsYearYearResponse,
    "AttendanceGetAttendanceHistoryAttendanceCodesResponse": AttendanceGetAttendanceHistoryAttendanceCodesResponse,
    "AttendanceGetAttendanceHistoryAttendanceCodesYearYearResponse": AttendanceGetAttendanceHistoryAttendanceCodesYearYearResponse,
    "StaffGetStaffInformationResponse": StaffGetStaffInformationResponse,
    "StaffCreateStaffInformationCreateResponse": StaffCreateStaffInformationCreateResponse,
    "StaffUpdateStaffInformationUpdateResponse": StaffUpdateStaffInformationUpdateResponse,
    "SchedulingGetCourseInformationResponse": SchedulingGetCourseInformationResponse,
    "SchedulingGetCourseDataChangesResponse": SchedulingGetCourseDataChangesResponse,
    "SchedulingGetSectionsFromMasterScheduleResponse": SchedulingGetSectionsFromMasterScheduleResponse,
    "SchedulingGetSectionDataChangesFromMasterScheduleResponse": SchedulingGetSectionDataChangesFromMasterScheduleResponse,
    "SchedulingGetStaffClassesSectionsResponse": SchedulingGetStaffClassesSectionsResponse,
    "SchedulingGetSectionClassRosterResponse": SchedulingGetSectionClassRosterResponse,
    "SchedulingGetSectionClassRosterDataChangesResponse": SchedulingGetSectionClassRosterDataChangesResponse,
    "SchedulingGetSectionFromSchedulingMasterScheduleResponse": SchedulingGetSectionFromSchedulingMasterScheduleResponse,
    "SchedulingCreateSectionFromSchedulingMasterScheduleResponse": SchedulingCreateSectionFromSchedulingMasterScheduleResponse,
    "GradebookGetGradebookInformationResponse": GradebookGetGradebookInformationResponse,
    "GradebookGetGradebookInformationSchoolsSchoolCodeSectionsSectionNumberGradebooksResponse": GradebookGetGradebookInformationSchoolsSchoolCodeSectionsSectionNumberGradebooksResponse,
    "GradebookGetGradebookInformationGradebooksGradebookNumberResponse": GradebookGetGradebookInformationGradebooksGradebookNumberResponse,
    "GradebookGetAssignmentInformationResponse": GradebookGetAssignmentInformationResponse,
    "GradebookGetAssignmentInformationAssignmentsUniqueIdResponse": GradebookGetAssignmentInformationAssignmentsUniqueIdResponse,
    "GradebookUpdateUpdatingAssignmentInformationResponse": GradebookUpdateUpdatingAssignmentInformationResponse,
    "GradebookUpdateUpdatingAssignmentInformationAssignmentsUniqueIdResponse": GradebookUpdateUpdatingAssignmentInformationAssignmentsUniqueIdResponse,
    "GradebookCreateInsertingANewAssignmentResponse": GradebookCreateInsertingANewAssignmentResponse,
    "GradebookGetFinalMarkRangesResponse": GradebookGetFinalMarkRangesResponse,
    "GradebookGetGradebookStudentInformationResponse": GradebookGetGradebookStudentInformationResponse,
    "GradebookGetAssignmentScoresResponse": GradebookGetAssignmentScoresResponse,
    "GradebookGetAssignmentScoresAssignmentsUniqueIdScoresStudentIdResponse": GradebookGetAssignmentScoresAssignmentsUniqueIdScoresStudentIdResponse,
    "GradebookCreateUpdatingAssignmentScoresResponse": GradebookCreateUpdatingAssignmentScoresResponse,
    "GradebookCreateUpdatingAssignmentScoresAssignmentsUniqueIdScoresResponse": GradebookCreateUpdatingAssignmentScoresAssignmentsUniqueIdScoresResponse,
}
