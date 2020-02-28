class Person:

    def set_name(self, name):
        self.name = name

    def set_lastname(self, lastname):
        self.lastname = lastname


p1 = Person()
p1.set_name("John")
p1.set_lastname("Doe")

print(f"{p1.name} {p1.lastname}")
