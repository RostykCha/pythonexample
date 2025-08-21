print("Enter a nimber below:")
value = input()

print(value)
match int(value):
    case 10:
        print("Ok")
    case 15:
        print("Warning")
    case _:
        print("Unknown")
