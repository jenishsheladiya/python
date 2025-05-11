
# library management for books 
class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def borrow_book(self, borrowbook):
        if (borrowbook >= self.available):
            print("not enough available book")
        else:
            self.available -= borrowbook
            print(f"borrow book : {borrowbook} ,available book: {self.available}")

    def return_book(self, returnbook):
        self.available += returnbook
        print(f"return book: {returnbook}, available book: {self.available}")

b1 = Book("mahabharat", "valmiki", 25)
b1.borrow_book(10)
b1.return_book(5)
