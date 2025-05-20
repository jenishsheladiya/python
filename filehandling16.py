# Reading the contents of a file
with open("example1.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)
