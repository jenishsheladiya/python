# Shopping Wallet System
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def spend(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance

w = Wallet(1000)
w.spend(200)
print(w.check_balance())
