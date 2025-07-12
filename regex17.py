# Find Hashtags
import re
tweet = "Learning #Python and #Regex is fun"
hashtags = re.findall(r"#\w+", tweet)
print(hashtags)  # ['#Python', '#Regex']
