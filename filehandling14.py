
# Reverse lines
with open("story.txt", "r")as f:
    content = f.read()

with open("reversed.txt", "w")as f:
    for line in reversed(content):
        f.write(line)