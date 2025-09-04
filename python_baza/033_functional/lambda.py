animals1 = ["Dog", "Cat", "ELEPHANT"]
animals2 = map(lambda s: s.lower(), animals1)

print(list(animals2))

funcs = []
for i in range(10):
    funcs.append(lambda i=i: print(i))

for f in funcs:
    f()