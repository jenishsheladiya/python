
# bank account to withdraw and deposite money
class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance

    def deposite(self, amount):
        self.amount = amount
        self.balance += self.amount
        print(f"bank account credited: {self.amount},total balance : {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
        print(f"bank account debited: {self.amount}, total balance :{self.balance}")

b1 = BankAccount(95540, 5000)
b1.deposite(200)
b1.withdraw(500)
