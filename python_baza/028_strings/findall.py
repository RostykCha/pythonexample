import re

menu = """
1. Fish
2. Bread
3. Peppers
4. Potatoes
"""

result = re.findall(r"(\d+)", menu)
print(result)