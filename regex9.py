# Validate a Mobile Number (10 digits)
import re
number = "9876543210"
print(bool(re.match(r"^[6-9]\d{9}$", number)))  # True
