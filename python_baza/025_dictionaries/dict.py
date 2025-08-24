month = {
    "Jan": "January",
    "Dec": "December",
    "Feb": "February",
}

print(month["Jan"])
month["Apr"] = "April"
month["Jan"] = "April"
print(month)

for item in month:
    print(item, month[item])

for itemKey, itemValue in month.items():
    print(itemKey, itemValue)