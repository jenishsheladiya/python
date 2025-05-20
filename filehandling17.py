# Appending new data to an existing file
with open("example1.txt", "a") as file:
    file.write("\nThis line was appended later.")

# Reading again to check
with open("example1.txt", "r") as file:
    print(file.read())
