fruits = "apple", "pear", "orange"
days = "Mon", "Tue", "Wed"

for i, fruite in enumerate(fruits):
    print(i, fruite)

for fruite, day in zip(fruits, days):
    print(fruite, day)