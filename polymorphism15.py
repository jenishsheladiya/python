# Student Info
class Student:
    def info(self, name=None):
        if name:
            print(f"Hello {name}")
        else:
            print("Hello Student")

s = Student()
s.info()
s.info("Jenish")
