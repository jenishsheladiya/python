
# write and read file
with open("notes.txt", "w") as f:
    f.write("Python is fun!")
    
with open("notes.txt", "r") as f:
    content  = f.read()
    print(content)