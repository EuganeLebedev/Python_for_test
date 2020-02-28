class Person:
    def __init__(self, name, lastname):
        self.nanme = name
        self.lastname = lastname

    def to_dict(self):
        return {
                "name": self.name,
                "lastname": self.lastname
                }
    @staticmethod #Не получает объект первым параметром
    def foo():
        pass

    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['lastname']

Person.foo()

person = Person.from_dict({})
p1 = Person("Ivan", "Ivanov")
