class Person:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        return "NON EXISTING"

p1 = Person("Ivan")
print(p1.lastname)
print(p1.foo)
print(p1.bark)
