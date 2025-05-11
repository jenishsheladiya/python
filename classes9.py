
# E-commerce Product class
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def buy(self, quantity):
        if quantity > self.stock:
            print("not enough stock available!")
        else:
            self.stock -= quantity
            total_cost = quantity * self.price
            print(f"you bought {quantity} {self.name} for {total_cost}. reamaining stock: {self.stock}")

p1 = Product("laptop", 50000, 10)
p1.buy(2)
