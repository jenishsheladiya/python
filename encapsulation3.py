# Student Grades System
class Student:
    def __init__(self, name):
        self.__name = name
        self.__grade = None

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade

    def get_grade(self):
        return self.__grade

s = Student("Jenish")
s.set_grade(85)
print(s.get_grade())  # Output: 85
