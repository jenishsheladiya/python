# Match Time (24-hour format)
import re
time = "23:59"
print(bool(re.match(r"([01]\d|2[0-3]):[0-5]\d", time)))  # True
