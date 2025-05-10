
# check the order1 greater than order2
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("chips", 20)
odr2 = Order("kurkure", 10)
print(odr1 > odr2)
