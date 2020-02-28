class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, salary):
        super().__init__(name)
        self.salary = salary


class Client(Person):
    def __init__(self, name, phone):
        super().__init__(name)
        self.phone = phone


Client.__mro__
