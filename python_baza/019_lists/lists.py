fruits = ["apple", "orange", "grape"]
animals = "dog", "cat", "mouse"
food = ("pizza", "pasta", "borsch")

print(type(fruits))
print(type(animals))
print(type(food))

fruits += ["melon"]
fruits.append("NewMelon")
fruits.remove("orange")
fruits[0] = "newApple"
print(fruits)

fruits_tuple  = tuple(fruits)
print(type(fruits_tuple))