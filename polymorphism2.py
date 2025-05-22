
# Method Overriding
class Employee:
    def work(self):
        print("Employee works")

class Developer(Employee):
    def work(self):
        print("Developer writes code")

class Designer(Employee):
    def work(self):
        print("Designer creates designs")

e = Employee()
d1 = Developer()
d2 = Designer()
e.work()
d1.work()
d2.work()