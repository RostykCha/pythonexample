try:
    print(1/0)
except Exception as someObject:
    print("Cached", someObject)
finally:
    print("Finally")