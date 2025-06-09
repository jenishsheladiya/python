# Count vowels in a string
text = "hello world"
vowels = 0
for ch in text:
    if ch in "aeiou":
        vowels += 1
print("Vowels:", vowels)
