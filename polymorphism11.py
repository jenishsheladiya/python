# Employees with Different Salaries
class Manager:
    def salary(self):
        print("Salary = 80000")

class Developer:
    def salary(self):
        print("Salary = 50000")

for emp in (Manager(), Developer()):
    emp.salary()
