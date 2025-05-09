# Payment system using abstractmethod
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# Testing
payment1 = CreditCardPayment()
payment2 = UpiPayment()

payment1.pay(500)
payment2.pay(250)
