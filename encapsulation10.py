# Movie Ticket Booking
class MovieTicket:
    def __init__(self, movie):
        self.movie = movie
        self.__seats = 50

    def book_ticket(self, qty):
        if qty <= self.__seats:
            self.__seats -= qty
            print(f"{qty} tickets booked for {self.movie}")
        else:
            print("Not enough seats")

m = MovieTicket("Avengers")
m.book_ticket(5)
