
# Movie ticket Booking system
class Movie:
    def __init__(self, name, available_seats):
        self.name = name
        self.available_seats = available_seats

    def book_ticket(self, quantity):
        if quantity > self.available_seats:
            print("Not enough seats available!")
        else:
            self.available_seats -= quantity
            print(f"{quantity} ticket(s) booked for {self.name}. remaining seats: {self.available_seats}")
m1 = Movie("Avengers", 10)
m1.book_ticket(3)
m1.book_ticket(8)