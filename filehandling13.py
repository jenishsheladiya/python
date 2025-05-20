
# Search for a word
user = input("Enter a word: ")
with open("story.txt", "r")as f:
    content = f.read()
    if user in content:
        print("Found!")
    else:
        print("Not Found.")
