# Factorial of a number
n = int(input("Enter a number: "))
fact = 1
while n > 1:
    fact *= n
    n -= 1
print("Factorial is:", fact)
