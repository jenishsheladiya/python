# Bank System accounts using abstractmethod
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest: 4%")

class FixedDepositAccount(BankAccount):
    def calculate_interest(self):
        print("Fixed Deposit Interest: 6.5%")

s = SavingsAccount()
f = FixedDepositAccount()
s.calculate_interest()
f.calculate_interest()
