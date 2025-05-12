
# ATM simulator
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(f"Total balance is : {self.__balance}")

    def deposit(self, amount):
        self.__balance += amount
        print(f"money deposite : {amount}, Total balance is : {self.__balance}")

    def withdraw(self, amount):
        if(amount > self.__balance):
            print("not enough balance on your account")
        else:
            self.__balance -= amount
            print(f"money withdraw: {amount}, total balance is : {self.__balance}")

a1 = ATM(50000)
a1.check_balance()
a1.deposit(5000)
a1.withdraw(3000)
