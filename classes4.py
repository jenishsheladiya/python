
# perform student details 
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"student name is :{self.name} and age is :{self.age} and student grade is: {self.grade}")

s1 = Student("jenish", 21, 98)
s1.display_info()