#  Calculator Polymorphism
class Add:
    def calculate(self, a, b):
        return a + b

class Multiply:
    def calculate(self, a, b):
        return a * b

calc1 = Add()
calc2 = Multiply()
print(calc1.calculate(2, 3))
print(calc2.calculate(2, 3))
