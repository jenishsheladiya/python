#  School System (Super Keyword)
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def teach(self):
        print(f"{self.name} teaches {self.subject}")

t = Teacher("Ms. Neha", "Math")
t.teach()
