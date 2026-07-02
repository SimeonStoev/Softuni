from project3.employee import Employee
from project3.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."