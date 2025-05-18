# Shopping Cart
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

p = Product("Phone", 500)
print(p.get_price())  # Output: 500
