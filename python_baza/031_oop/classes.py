from itrem import Itrem

class Person(Itrem):
    _count = 0

    def __init__(self, name, surname):
        Person._count += 1
        self._protectedName = name
        self.__privateSurname = surname

    def __str__(self):
        return f"Hello I am {self._protectedName} {self.__privateSurname}"

    def __repr__(self):
        return f'Person("{self._protectedName}")'

    def eating(self):
        print(f"I am {self._protectedName} and I eat")

    @classmethod
    def class_method(cls):
        print(f"works with class {cls._count}")

    @staticmethod
    def static_method():
        print("no self, no cls")


class Company:
    def __init__(self, place):
        self._place = place

    def do_work(self):
        print("Working")


class Employee(Person, Company):
    def __init__(self, name, surname, place):
        super().__init__(name, surname)
        self._place = place
        print("Employee constructor")

    def go_on_holiday(self):
        print("I am going to holiday")

    def eating(self):
        print(f"I can't eat on work at {self._place}")


e = Employee("Harry", "Days", "DMW")
e2 = Employee("Harry", "Days", "DMW")

e.eating()
e.go_on_holiday()
e.do_work()
e.class_method()
e.static_method()

print(Person._count)
