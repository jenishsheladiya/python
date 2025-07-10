# Validate Email
import re

email = "test@example.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
print(bool(re.match(pattern, email)))  # True
