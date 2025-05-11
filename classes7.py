
# employee class and salary calculation
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def apply_bonus(self, bonus_percentage):
        bonus = self.salary * (bonus_percentage / 100)
        self.salary += bonus
        print(f"bonus received : {bonus_percentage} total salary : {self.salary}")

e1 = Employee("Jenish", "manager", 50000)
e1.apply_bonus(10)
