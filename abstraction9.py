# Payment System (Abstract Payment Method)
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using PayPal.")

payment = CreditCardPayment()
payment.make_payment(500)
