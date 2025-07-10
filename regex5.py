# Replace All Digits with '#'
import re
text = "My pin is 7890"
masked = re.sub(r"\d", "#", text)
print(masked)  # My pin is ####

