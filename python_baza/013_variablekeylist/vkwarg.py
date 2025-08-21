def details(name, **dsfds):
    print("Name", name)

    print(type(dsfds))
    print(dsfds)

    if "height" in dsfds:
        print("User height", dsfds["height"])

    for key in dsfds:
        print(key, dsfds[key])

details("Brian", height=176, weight=75, age=17)