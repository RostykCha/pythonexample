animals1 = ["Dog", "Cat", "ELEPHANT", "bird", "LiOn", "afish"]
animals2 = filter(lambda s: "a" in s, animals1)

print(list(animals2))