# Find All Capital Words
import re
text = "I love India and USA and UK"
capitals = re.findall(r"\b[A-Z]{2,}\b", text)
print(capitals)  # ['USA', 'UK']
