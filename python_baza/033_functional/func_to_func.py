def greet():
    print("Greeting")

def eat():
    print("Eating")

def run(func):
    print("Will run function")
    func()

run(greet)
run(eat)