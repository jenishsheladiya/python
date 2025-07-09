#  Find All Words in a Sentence
import re

text = "Python is great!"
words = re.findall(r"\w+", text)
print(words)  # ['Python', 'is', 'great']
