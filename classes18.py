# Smartphone Inventory
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Inventory:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)
        print(f"{phone.model} added to inventory.")

    def display_phones(self):
        for phone in self.phones:
            print(f"{phone.brand} {phone.model} - ₹{phone.price}")

inv = Inventory()
inv.add_phone(Smartphone("Apple", "iPhone 14", 80000))
inv.add_phone(Smartphone("Samsung", "S23", 70000))
inv.display_phones()
