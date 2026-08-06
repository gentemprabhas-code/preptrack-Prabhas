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

    if student_name.strip() != "":
        break

    print("Student name cannot be empty.")
    print()

print()