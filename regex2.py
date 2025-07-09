# Check if String Starts with "Hello"
import re
text = "Hello World"
match = re.match(r"Hello", text)
print(bool(match))  # True
