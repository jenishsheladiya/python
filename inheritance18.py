# Book Library (Class Inheritance with Additional Method)
class Book:
    def __init__(self, title):
        self.title = title

class Ebook(Book):
    def download(self):
        print(f"Downloading {self.title}...")

class Audiobook(Book):
    def listen(self):
        print(f"Listening to {self.title}...")

e = Ebook("Python 101")
a = Audiobook("Learning Python")
e.download()
a.listen()
