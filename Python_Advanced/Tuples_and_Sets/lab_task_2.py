import statistics

students = {}

number_of_students = int(input())

for _ in range(number_of_students):
    student_data = input().split()
    student = student_data[0]
    grade = float(student_data[1])
    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)

for student, grades in students.items():
    print(f"{student} -> {' '.join(f'{grade:.2f}' for grade in grades)} (avg: {statistics.mean(grades):.2f})")