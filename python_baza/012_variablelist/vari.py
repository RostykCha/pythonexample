def catalogue(name, *whateverawd):
    print(name)

    print("Type: ", type(whateverawd))

    for value in whateverawd:
        print(value)


catalogue("Animals", "dog", "cat", "fish")