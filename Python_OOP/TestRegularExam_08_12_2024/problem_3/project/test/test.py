from project.senior_student import SeniorStudent

from unittest import TestCase, main

class TestSeniorStudent(TestCase):
    def setUp(self):
        self.senior_student = SeniorStudent("id: one", "student", 4.5)
        self.other_senior_student = SeniorStudent("id: two", "other", 3.5)

    def test_init(self):
        self.assertEqual(self.senior_student.student_id, "id: one")
        self.assertEqual(self.senior_student.name, "student")
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        self.assertEqual(self.senior_student.colleges, set())

    def test_get_student_id(self):
        self.assertEqual(self.senior_student.student_id, "id: one")

    def test_set_student_id_with_incorrect_value_raise(self):
        self.assertEqual(self.senior_student.student_id, "id: one")
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_id = "    id1    "
        self.assertEqual(str(ex.exception), "Student ID must be at least 4 digits long!")
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_id = "        "
        self.assertEqual(str(ex.exception), "Student ID must be at least 4 digits long!")

    def test_set_student_id_with_correct_value(self):
        self.assertEqual(self.senior_student.student_id, "id: one")
        self.senior_student.student_id = "  id: two   "
        self.assertEqual(self.senior_student.student_id, "id: two")
        self.senior_student.student_id = "id: three"
        self.assertEqual(self.senior_student.student_id, "id: three")

    def test_get_name(self):
        self.assertEqual(self.senior_student.name, "student")

    def test_set_name_with_incorrect_value_raise(self):
        self.assertEqual(self.senior_student.name, "student")
        with self.assertRaises(ValueError) as ex:
            self.senior_student.name = ""
        self.assertEqual(str(ex.exception), "Student name cannot be null or empty!")

        with self.assertRaises(ValueError) as ex:
            self.senior_student.name = "   "
        self.assertEqual(str(ex.exception), "Student name cannot be null or empty!")

    def test_set_name_with_correct_value(self):
        self.assertEqual(self.senior_student.name, "student")
        self.senior_student.name = "student studentov"
        self.assertEqual(self.senior_student.name, "student studentov")

    def test_get_student_gpa(self):
        self.assertEqual(self.senior_student.student_gpa, 4.5)

    def test_set_student_gpa_with_incorrect_value_raise(self):
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = 1.0
        self.assertEqual(str(ex.exception), "Student GPA must be more than 1.0!")

        with self.assertRaises(ValueError) as ex:
            self.senior_student.student_gpa = 0.9
        self.assertEqual(str(ex.exception), "Student GPA must be more than 1.0!")

    def test_set_student_gpa_with_correct_value(self):
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        self.senior_student.student_gpa = 3.5
        self.assertEqual(self.senior_student.student_gpa, 3.5)
        self.senior_student.student_gpa = 5.5
        self.assertEqual(self.senior_student.student_gpa, 5.5)
        self.senior_student.student_gpa = 5
        self.assertEqual(self.senior_student.student_gpa, 5)

    def test_senior_student_apply_to_college(self):
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        self.assertEqual(self.senior_student.colleges, set())
        college_application = self.senior_student.apply_to_college(5.0, "Harvard")
        self.assertEqual(college_application, 'Application failed!')

        college_application = self.senior_student.apply_to_college(4, "MIT")
        self.assertEqual(college_application, f"{self.senior_student.name} successfully applied to MIT.")
        college_set_check = self.senior_student.colleges == {"MIT"}
        self.assertEqual(college_set_check, True)

        college_application = self.senior_student.apply_to_college(4.30, "London University")
        self.assertEqual(college_application, f"{self.senior_student.name} successfully applied to London University.")
        college_set_check = self.senior_student.colleges == {"MIT", "LONDON UNIVERSITY"}
        self.assertEqual(college_set_check, True)

    def test_update_gpa(self):
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        update_gpa_result = self.senior_student.update_gpa(1)
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        self.assertEqual(update_gpa_result, "The GPA has not been changed!")
        update_gpa_result = self.senior_student.update_gpa(0.9)
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        self.assertEqual(update_gpa_result, "The GPA has not been changed!")
        update_gpa_result = self.senior_student.update_gpa(3.5)
        self.assertEqual(self.senior_student.student_gpa, 3.5)
        self.assertEqual(update_gpa_result, "Student GPA was successfully updated.")
        update_gpa_result = self.senior_student.update_gpa(5.5)
        self.assertEqual(self.senior_student.student_gpa, 5.5)
        self.assertEqual(update_gpa_result, "Student GPA was successfully updated.")
        update_gpa_result = self.senior_student.update_gpa(5)
        self.assertEqual(self.senior_student.student_gpa, 5)
        self.assertEqual(update_gpa_result, "Student GPA was successfully updated.")

    def test_equality_between_two_students_by_gpa(self):
        self.assertEqual(self.senior_student.student_gpa, 4.5)
        self.assertEqual(self.other_senior_student.student_gpa, 3.5)
        self.assertFalse(self.senior_student == self.other_senior_student)
        self.other_senior_student.student_gpa = 4.5
        self.assertTrue(self.senior_student == self.other_senior_student)

if __name__ == '__main__':
    main()