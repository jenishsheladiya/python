# Parking Lot System
class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.occupied_spots = 0

    def park_car(self):
        if self.occupied_spots < self.total_spots:
            self.occupied_spots += 1
            print("Car parked.")
        else:
            print("Parking full!")

    def leave_car(self):
        if self.occupied_spots > 0:
            self.occupied_spots -= 1
            print("Car left.")
        else:
            print("No cars to leave.")

    def status(self):
        print(f"Spots available: {self.total_spots - self.occupied_spots}")

p1 = ParkingLot(5)
p1.park_car()
p1.park_car()
p1.leave_car()
p1.status()
