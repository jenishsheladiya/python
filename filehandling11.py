# Word Frequency Counter
with open("story.txt", "r")as f:
    content = f.read()
    print(content.count("the"))

