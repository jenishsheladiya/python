
# Using super()
class Vehicle:
    def __init__ (self, brand):
        self.brand = brand
    
class Car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand)
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Brand : {self.brand}, Model : {self.model}, Year : {self.year}")

c1= Car("toyota", "Fortuner", 2020)
c1.car_info()