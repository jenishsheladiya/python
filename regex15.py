#  Remove Special Characters
import re
txt = "Hello@#World!$"
clean = re.sub(r"[^\w\s]", "", txt)
print(clean)  # HelloWorld
