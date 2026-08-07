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
