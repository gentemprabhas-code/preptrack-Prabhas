#==================================================
#              PREPTRACK APPLICATION
#==================================================
print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)
# --------------------------------------------------
# 1. COLLECT STUDENT DETAILS
# --------------------------------------------------
print("=" * 50)
print("              COLLECT STUDENT DETAILS")
print("=" * 50)
#student_name validation
while True:
    student_name = input("Enter student name: ")

    if student_name=="":
        print ("Student name cannot be empty, Try again.")
    else:
        break
#registration_number validation
registration_number = input("Enter registration number: ")
#graduation_year
while True:
    graduation_year = int(input("Enter graduation year: "))
    if graduation_year >= 2025 and graduation_year <= 2027:
        print("Eligible for placement.")
        break
    else:
        print("Not eligible for placement.")
#attendance validation
while True:
    attendance = float(input("Enter attendance percentage: "))
    if attendance >= 0 and attendance <= 100:
        break
    else:
        print("Invalid attendance. Enter a value between 0 and 100.")
#Project-Completion Input
while True:
    project_input = input("Has the student completed the required project? (yes/no): ").lower()
    if project_input in ["yes", "no"]:
        break
    else:
        print("Invalid input. Enter yes or no.")
#Profile-Verification Input
while True:
    profile_input = input("Is the student profile verified? (yes/no): ").lower()
    if profile_input in ["yes", "no"]:
        break
    else:
        print("Invalid input. Enter yes or no.")
# --------------------------------------------------
# 2. INITIALIZE COUNTERS AND ACCUMULATORS
# --------------------------------------------------
print("=" * 50)
print("              INITIALIZE COUNTERS AND ACCUMULATORS")
print("=" * 50)
total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0
#Process Seven Practice Days
print("=" * 50)
print("              PROCESS SEVEN PRACTICE DAYS")
print("=" * 50)

for day in range(1, 8):
    while True:
        score = int(input(f"Enter Day {day} score (0-100) or -1 for absent: "))
        if score == -1 or (score >= 0 and score <= 100):
            break
        else:
            print("Invalid score. Try again.")

    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
    else:
        attempted_days += 1
        total_score += score
        #Classify the score
        if score >= 75 and score <= 100:
            classification = "Strong"
            strong_days += 1
        elif score >= 60 and score <= 74:
            classification = "Satisfactory"
            satisfactory_days += 1
        elif score >= 40 and score <= 59:
            classification = "Needs Improvement"
            improvement_days += 1
        else:
            classification = "Critical"
            critical_days += 1
        print(f"Day {day} Result: {classification}")

        #Passed / Failed
        if score >= 60:
            passed_days += 1
        else:
            failed_days += 1

        #Track highest and lowest
        if not first_attempt_found:
            highest_score = score
            highest_score_day = day
            lowest_score = score
            lowest_score_day = day
            first_attempt_found = True
        else:
            if score > highest_score:
                highest_score = score
                highest_score_day = day
            if score < lowest_score:
                lowest_score = score
                lowest_score_day = day

        #First critical score
        if score < 40:
            if not critical_score_found:
                critical_score_found = True
                first_critical_day = day
                first_critical_score = score
    print()
# ---------------------------------------------------------
# 4. CALCULATE THE AVERAGE
# ---------------------------------------------------------
print("=" * 50)
print("              CALCULATE THE AVERAGE")
print("=" * 50)
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0
print(f"Average Score: {average_score}")
print()
# --------------------------------------------------
# 5. CREATE ELIGIBILITY CONDITIONS
# --------------------------------------------------
print("=" * 50)
print("              CREATE ELIGIBILITY CONDITIONS")
print("=" * 50)
graduation_eligible = (graduation_year >= 2025 and graduation_year <= 2027)
attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4
project_completed = (project_input == "yes")
profile_verified = (profile_input == "yes")

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)
print(graduation_eligible)
print(attendance_eligible)
print(practice_count_eligible)
print(average_eligible)
print(critical_score_clear)
print(passed_days_eligible)
print(project_completed)
print(profile_verified)
print(placement_ready)
print()
# ---------------------------------------------------------
# 6. FINAL STATUS PRIORITY
# ---------------------------------------------------------
print("=" * 50)
print("              FINAL STATUS PRIORITY")
print("=" * 50)
print()
if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    primary_blocker = "No practice was attempted"
    next_action = "Attempt the required coding practices"
elif critical_score_found:
    final_status = "Critical Support Required"
    primary_blocker = "A critical score exists"
    next_action = "Revise the concepts from the first critical day"
elif attempted_days < 6:
    final_status = "Practice Incomplete"
    primary_blocker = "Fewer than six practices were attempted"
    next_action = "Complete at least six practice days"
elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    primary_blocker = "Fewer than four practices were passed"
    next_action = "Pass at least four coding practices"
elif average_score < 70:
    final_status = "Practice Improvement Required"
    primary_blocker = "Average score is below 70"
    next_action = "Improve the average score to at least 70"
elif attendance < 75:
    final_status = "Attendance Improvement Required"
    primary_blocker = "Attendance is below 75"
    next_action = "Improve attendance to at least 75 percent"
elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    primary_blocker = "Graduation year is not eligible"
    next_action = "Check the eligible graduation-year requirement"
elif not project_completed:
    final_status = "Application On Hold"
    primary_blocker = "Project is incomplete"
    next_action = "Complete the required project"
elif not profile_verified:
    final_status = "Application On Hold"
    primary_blocker = "Profile is not verified"
    next_action = "Complete profile verification"
else:
    final_status = "Ready for Mock Interview"
    primary_blocker = "None"
    next_action = "Proceed to placement mock interviews"
    print(f"final_status: {final_status}")
    print(f"primary_blocker: {primary_blocker}")
    print(f"next_action: {next_action}")
print()

# ---------------------------------------------------------
# 7. FINAL REPORT
# ---------------------------------------------------------
print("=" * 50)
print("              FINAL REPORT")
print("=" * 50)
print()
if first_attempt_found:
    highest_score_display = highest_score
    highest_score_day_display = f"Day {highest_score_day}"
    lowest_score_display = lowest_score
    lowest_score_day_display = f"Day {lowest_score_day}"
else:
    highest_score_display = "Not Available"
    highest_score_day_display = "Not Available"
    lowest_score_display = "Not Available"
    lowest_score_day_display = "Not Available"

if critical_score_found:
    first_critical_day_display = f"Day {first_critical_day}"
    first_critical_score_display = first_critical_score
    critical_score_found_display = "Yes"
else:
    first_critical_day_display = "Not Applicable"
    first_critical_score_display = "Not Applicable"
    critical_score_found_display = "No"

project_completed_display = "Yes" if project_completed else "No"
profile_verified_display = "Yes" if profile_verified else "No"
print(f"attendance eligible: {attendance_eligible}")
print(f"practice count eligible: {practice_count_eligible}")
print(f"average eligible: {average_eligible}")
print(f"critical score clear: {critical_score_clear}")
print(f"passed days eligible: {passed_days_eligible}")
print(f"project completed: {project_completed}")
print(f"profile verified: {profile_verified}")
print(f"placement ready: {placement_ready}")


print("=" * 50)
print("              PREPTRACK REPORT")
print("=" * 50)
print()

print("STUDENT PROFILE")
print()
print(f"Student Name             : {student_name}")
print(f"Registration Number      : {registration_number}")
print(f"Graduation Year          : {graduation_year}")
print(f"Attendance               : {attendance}")
print(f"Project Completed        : {project_completed_display}")
print(f"Profile Verified         : {profile_verified_display}")
print()

print("PRACTICE SUMMARY")
print()
print(f"Total Practice Days      : 7")
print(f"Attempted Days           : {attempted_days}")
print(f"Absent Days              : {absent_days}")
print(f"Passed Days              : {passed_days}")
print(f"Failed Days              : {failed_days}")
print()
print(f"Strong Days              : {strong_days}")
print(f"Satisfactory Days        : {satisfactory_days}")
print(f"Needs Improvement Days   : {improvement_days}")
print(f"Critical Days            : {critical_days}")
print()

print("PERFORMANCE ANALYSIS")
print()
print(f"Total Score              : {total_score}")
print(f"Average Score            : {round(average_score, 2)}")
print(f"Highest Score            : {highest_score_display}")
print(f"Highest Score Day        : {highest_score_day_display}")
print(f"Lowest Score             : {lowest_score_display}")
print(f"Lowest Score Day         : {lowest_score_day_display}")
print()

print("CRITICAL SCORE INFORMATION")
print()
print(f"Critical Score Found     : {critical_score_found_display}")
print(f"First Critical Day       : {first_critical_day_display}")
print(f"First Critical Score     : {first_critical_score_display}")
print()

print("FINAL DECISION")
print()
print(f"Final Status             : {final_status}")
print(f"Primary Blocker          : {primary_blocker}")
print(f"Next Action              : {next_action}")
print()
print("=" * 50)


