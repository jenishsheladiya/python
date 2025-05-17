# Employee Salary
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_salary(self):
        print(f"{self.name}'s salary is {self.__salary}")

e = Employee("Amit", 40000)
e.show_salary()  # Output: Amit's salary is 40000
