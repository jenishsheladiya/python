# Duck Typing
class Car:
    def start(self):
        print("Car started")
    
class Bike:
    def start(self):
        print("Bike started")

def start_vehicle(vehicle):
    vehicle.start()

c1 = Car()
b1 = Bike()
start_vehicle(c1)
start_vehicle(b1)
