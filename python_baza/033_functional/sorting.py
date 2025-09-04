animals1 = ["Dog", "Cat", "ELEPHANT", "bird", "LiOn", "Afish"]
animals2 = sorted(animals1, reverse=True, key=lambda s: len(s))

print(animals2)
