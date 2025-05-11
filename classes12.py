
# Shopping cart system:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"added {product.name} to the cart.")

    def total_price(self):
        total = sum(item.price for item in self.items)
        print(f"Total cart price: {total}")

c1 = Cart()
p1 = Product("phone", 500)
p2 = Product("Headphone", 100)

c1.add_product(p1)
c1.add_product(p2)
c1.total_price()
