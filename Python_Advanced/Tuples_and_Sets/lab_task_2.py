students = {}

number_of_students = int(input())

for _ in range(number_of_students):
    student_data = input().split()
    student = student_data[0]
    grade = float(student_data[1])
    if student not in students:
        students[student] = []
    students[student].append(grade)

for student, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join(f'{grade:.2f}' for grade in grades)} (avg: {avg_grade:.2f})")