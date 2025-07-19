# search a number x in this tuple using while loop

tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 25
n = 0
while n<len(tuple):
    if(tuple[n] == x):
        print(f"Found at idx = {n}")
    else:
        print("Searching")
    n += 1
