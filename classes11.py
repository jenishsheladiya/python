
# libray system with book borrowing
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"you have borrowed {self.title}")
        else:
            print(f"{self.title} is not available!")

    def return_book(self):
        self.available = True
        print(f"you have returned {self.title}")

b1 = Book("python basics", "john doe")
b1.borrow_book()
b1.borrow_book()
b1.return_book()
