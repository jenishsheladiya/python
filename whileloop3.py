# repeatedly asks the user to enter a positive number using while loop

while True:
    user = int(input("Enter a positive number: "))
    if(user < 0):
        print("Loop terminted!")
        break
    elif(user == 0):
        print("Zero is not allowed!")
    else:
        print(f"you entered: {user}")
        