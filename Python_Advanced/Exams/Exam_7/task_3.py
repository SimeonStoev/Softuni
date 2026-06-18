def softuni_students(*args, **kwargs):
    invalid_students = []
    students = {}

    for course_id, student in args:
        if course_id not in kwargs:
            invalid_students.append(student)
        else:
            if student not in students:
                students[student] = []
            students[student].append(kwargs[course_id])

    students = dict(sorted(students.items(), key=lambda x: x[0]))

    result = ""

    for student, courses in students.items():
        for course in courses:
            result += f"*** A student with the username {student} has successfully finished the course {course}!\n"

    if len(invalid_students) > 0:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result
