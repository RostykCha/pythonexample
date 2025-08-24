import re

text = """
one
two
three
"""

result = re.search(r"(t.*)", text)

print("No match" if result is None else result.groups())