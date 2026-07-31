from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def test_init(self):
        student_one = Student("one")
        student_two = Student("two", {"english": ["good", "nice"]})
        self.assertEqual(student_one.name, "one")
        self.assertEqual(student_two.name, "two")
        self.assertEqual(student_one.courses, {})
        self.assertEqual(student_two.courses, {"english": ["good", "nice"]})

    def test_enroll_course_already_added(self):
        student = Student("one", {"english": ["good", "nice"]})
        result = student.enroll("english", ["great"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(student.courses, {"english": ["good", "nice", "great"]})

    def test_enroll_new_course_with_notes(self):
        student = Student("one", {"english": ["good", "nice"]})
        result = student.enroll("french", ["excellent"], "Y")
        self.assertEqual(result, "Course and course notes have been added.")
        self.assertEqual(student.courses, {"english": ["good", "nice"], "french": ["excellent"]})

    def test_enroll_new_course_without_notes(self):
        student = Student("one", {"english": ["good", "nice"]})
        result = student.enroll("travelling", ["good"], "N")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(student.courses, {"english": ["good", "nice"], "travelling": []})

    def test_add_notes_to_course_which_not_exists_raise(self):
        student = Student("one", {"english": ["good", "nice"]})
        with self.assertRaises(Exception) as ex:
            student.add_notes("french", "excellent")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_add_notes_to_course_which_exists(self):
        student = Student("one", {"english": ["good", "nice"]})
        result = student.add_notes("english", "excellent")
        self.assertEqual(result, "Notes have been updated")
        self.assertEqual(student.courses, {"english": ["good", "nice", "excellent"]})

    def test_leave_not_existing_course(self):
        student = Student("one", {"english": ["good", "nice"]})
        with self.assertRaises(Exception) as ex:
            student.leave_course("french")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

    def test_leave_existing_course(self):
        student = Student("one", {"english": ["good", "nice"]})
        result = student.leave_course("english")
        self.assertEqual(result, "Course has been removed")
        self.assertEqual(student.courses, {})

    def test_enroll_new_course_with_invalid_flag_falls_back_to_no_notes(self):
        student = Student("one")
        result = student.enroll("math", ["good"], "yes")
        self.assertEqual(result, "Course has been added.")
        self.assertEqual(student.courses, {"math": []})

    def test_enroll_existing_course_with_empty_notes(self):
        student = Student("one", {"english": ["good"]})
        result = student.enroll("english", [])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(student.courses, {"english": ["good"]})


if __name__ == '__main__':
    main()
