# Vehicle Fleet (Inheritance with Default Values)
class Vehicle:
    def __init__(self, wheels=4):
        self.wheels = wheels

class Bike(Vehicle):
    def __init__(self):
        super().__init__(2)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(6)

print(Bike().wheels)
print(Truck().wheels)
