
# Count Lines to file
with open("names.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))
