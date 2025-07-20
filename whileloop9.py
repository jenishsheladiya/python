# # guess the number game import random
import random
num = random.randint(1, 100)
user = None
while user != num:
    user = int(input("Enter a number: "))
    if (user == num):
        print("Number is right")
    elif(user < num):
        print("your number is small")
    elif(user > num):
        print("your number is BIG")

