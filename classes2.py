
# create a class bank account debit, credit and balance using methods.

class Account:
    def __init__(self,balance,accno):
        self.balance = balance
        self.accno = accno
    
    def debited(self):
        self.debited = int(input("Enter a debit money: "))
        self.balance += self.debited
        print(f"money was debited ${self.debited} and total balance:${self.balance}")

    def credited(self):
        self.credited = int(input("Enter a credit money: "))
        self.balance -= self.credited
        print(f"money was credited ${self.credited} and total balance : ${self.balance}")

a1 = Account(5000,12345)
print(a1.balance)
print(a1.accno)
a1.debited()
a1.credited()
