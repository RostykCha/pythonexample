# and, not , or
# True, False

raining = True
temperature = 20

if temperature > 20 and not raining:
    print("Weather fine")
elif not raining:
    print("At least it dry")
else:
    print("Stay home")

# ternary operator
mood = "good" if not raining else "bad, it's rain"
print(mood)

if not raining or temperature > 15:
    print("Go for a walk")
