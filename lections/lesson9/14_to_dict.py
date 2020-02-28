class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def to_dict(self):
        return {
            "name": self.name,
            "lastname": self.lastname
        }

    @staticmethod
    def foo():
        pass

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

person = Person.from_dict({})
Person.foo()
p1 = Person("Ivan", "Ivanov")

d = p1.to_dict()
