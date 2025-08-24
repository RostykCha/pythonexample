import re

text = "ID: 123 Some Corp. Serial: 345"
result = re.match(r".*", text)
print(result.group())