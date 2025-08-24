from collections import defaultdict

people = {
    "Ros": 28,
    "Luna": 2,
    "Kate": 24,
}

print(people["Ros"])
print(people.get("Babak", "This will be shown in case key is not existing"))

days = defaultdict(str)
days.update({"Mon": "Monday", "Tue": "Tuesday"})
print(days["Mon"])
print(days["Dao"])
print(days["Tue"])

