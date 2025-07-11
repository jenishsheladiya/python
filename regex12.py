# Match Dates (dd-mm-yyyy)
import re

date = "21-08-2025"
pattern = r"\b\d{2}-\d{2}-\d{4}\b"
print(bool(re.match(pattern, date)))  # True
