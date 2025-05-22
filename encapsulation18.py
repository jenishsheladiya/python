# Restaurant Table Booking
class Table:
    def __init__(self):
        self.__is_booked = False

    def book_table(self):
        self.__is_booked = True

    def check_status(self):
        return "Booked" if self.__is_booked else "Available"

tb = Table()
tb.book_table()
print(tb.check_status())
