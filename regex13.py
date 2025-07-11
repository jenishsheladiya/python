# Validate Username (5-10 characters)
import re
username = "user123"
print(bool(re.match(r"^\w{5,10}$", username)))  # True

