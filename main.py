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

