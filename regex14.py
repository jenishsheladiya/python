# Extract All Numbers from Text
import re

text = "Price is 40 and discount is 5%"
nums = re.findall(r"\d+", text)
print(nums)  # ['40', '5']
