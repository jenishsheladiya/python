# Regex (Regular Expression)
import re
text = "My email is hello@example.com"
match = re.search(r"\S+@\S+\.\S+", text)
print(match.group())
