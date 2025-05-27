# Bank Account System (Single Inheritance)
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")

class SavingsAccount(BankAccount):
    def apply_interest(self):
        self.balance *= 1.05
        print(f"Interest applied. New balance: {self.balance}")

acc = SavingsAccount(1000)
acc.deposit(500)
acc.apply_interest()
