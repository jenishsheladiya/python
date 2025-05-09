
# Employee Salary System
from abc import ABC, abstractmethod
class Employee():
    @abstractmethod
    def calculate_salary():
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary
    
class PartTimeEmployee():
    def __init__(self, hourly_rate, hours_work):
        self.hourly_rate = hourly_rate
        self.hours_work = hours_work
    
    def calculate_salary(self):
        return self.hourly_rate * self.hours_work
    
f1 = FullTimeEmployee(45000)
print(f1.calculate_salary())
p1 = PartTimeEmployee(20, 100)
print(p1.calculate_salary())



