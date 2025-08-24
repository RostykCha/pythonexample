import re

text = "az"
result = re.match(r"aaz", text)
print("No match" if result is None else result.group())
