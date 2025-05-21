# Library Book System
class Library:
    def __init__(self):
        self.__books = ["Python", "C++", "Java"]

    def get_books(self):
        return self.__books

    def add_book(self, book):
        self.__books.append(book)

lib = Library()
lib.add_book("JavaScript")
print(lib.get_books())
