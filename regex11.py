# Find HTML Tags
import re
html = "<p>This is a <b>bold</b> word</p>"
tags = re.findall(r"</?\w+>", html)
print(tags)  # ['<p>', '<b>', '</b>', '</p>']

