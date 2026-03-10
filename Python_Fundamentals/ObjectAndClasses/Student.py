class Student:

    def __init__(self, name, age, school):
        self.__name = name
        self.__age = age
        self.__school = school

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_school(self):
        return self.__school

    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    def set_school(self, school):
        self.__school = school

    def get_student_info(self):
        return f"Name: {self.__name}, age: {self.__age}, school: {self.__school}"

    def is_student_sophmor(self):
        return self.__age <= 14

student1 = Student("John", "25", "EG")
student2 = Student("Elon", "27", "PMG")
print(student1.get_student_info())
student1.set_age(20)
print(student1.get_student_info())
print(student2.get_student_info())
print(student1.is_student_sophmor())
