
# Add attribute
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_info(self):
        print(f"name : {self.name}, age : {self.age}, grade : {self.grade}")

s = Student("james", "21", "A")
s.show_info()