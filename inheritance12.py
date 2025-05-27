# E-Commerce System (Hierarchical Inheritance)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Electronic(Product):
    def warranty(self):
        print(f"{self.name} has 2-year warranty.")

class Clothing(Product):
    def size_chart(self):
        print(f"{self.name} sizes: S, M, L, XL")

e = Electronic("Laptop", 50000)
c = Clothing("T-Shirt", 500)
e.warranty()
c.size_chart()
