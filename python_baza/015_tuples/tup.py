mona = ("girl", "bot")
stuff = ("Charles", 7, True, "Dog", mona)

def printTupo(tupo):
    for element in tupo:
        print(element)

#stuff[2] = 9 We can't do it, tupo is immutable
printTupo(stuff)

#unpacing tupo
name, value, smth, fds, other = stuff
name2, value2, *other = stuff

print(name, value, smth, fds, other)
print(name2, value2, other)
