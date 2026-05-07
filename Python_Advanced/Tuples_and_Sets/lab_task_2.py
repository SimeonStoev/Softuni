# This script collects student names and their grades, stores them in a dictionary,
# and then prints each student's name, their grades, and the average grade.

# Initialize an empty dictionary to store student names as keys and lists of grades as values
students = {}

# Read the number of students from input
number_of_students = int(input())

# Loop for the number of students
for _ in range(number_of_students):
    # Read student data as a list of strings (name and grade)
    student_data = input().split()
    # Extract student name
    student = student_data[0]
    # Extract and convert grade to float
    grade = float(student_data[1])
    # If student not in dictionary, initialize empty list for grades
    if student not in students:
        students[student] = []
    # Append the grade to the student's list
    students[student].append(grade)

# Loop through each student and their grades
for student, grades in students.items():
    # Calculate the average grade
    avg_grade = sum(grades) / len(grades)
    # Print student name, grades formatted to 2 decimal places, and average
    print(f"{student} -> {' '.join(f'{grade:.2f}' for grade in grades)} (avg: {avg_grade:.2f})")
