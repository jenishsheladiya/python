# Remove All Vowels
text = "hello world"
no_vowels = "".join([char for char in text if char.lower() not in "aeiou"])
print(no_vowels)  # hll wrld
