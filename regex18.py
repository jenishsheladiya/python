# Validate Password (At least 8 chars, 1 digit, 1 uppercase)
import re
password = "Python123"
pattern = r"^(?=.*[A-Z])(?=.*\d).{8,}$"
print(bool(re.match(pattern, password)))  # True
