# Reading file line by line
with open("example1.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())
