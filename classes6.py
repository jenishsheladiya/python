

# car class with methods
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.model} engine is started....")

c1 = Car("toyota", "fortuner",  2022)
c1.start_engine()

