#  Extract Domain from Email
import re
email = "user123@gmail.com"
domain = re.search(r"@(\w+)\.", email).group(1)
print(domain)  # gmail
