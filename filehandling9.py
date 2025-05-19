
# User input to file
with open("names.txt", "w") as f:
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        f.write(name + "\n")
