#  Check for Only Alphabets
import re
name = "Jenish"
print(bool(re.fullmatch(r"[A-Za-z]+", name)))  # True

