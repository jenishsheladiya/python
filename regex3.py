# Search for Any Digit
import re
text = "My number is 12345"
found = re.search(r"\d+", text)
print(found.group())  # 12345
