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
