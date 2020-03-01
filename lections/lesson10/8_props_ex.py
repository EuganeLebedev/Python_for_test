class Person:
    def __init__(self, name, lastname):
        self._d = {
            "name": name,
            "lastname": lastname
        }

    @property
    def name(self):
        return self._d["name"]

    @name.setter
    def name(self, value):
        if value < 1000:
            raise ValueError("Less than 1000")

        self._d["name"] = value

    @property
    def lastname(self):
        return self._d["lastname"]

    @property
    def fullname(self):
        return f"{self._d['name']} {self._d['lastname']}"

    @fullname.setter
    def fullname(self, value):
        self._d['name'], self._d['lastname'] = value.split(" ")



p = Person("John", "Smith")
print(p.fullname)
print(p.name)
print(p.lastname)

p.fullname = "Ivan Ivanov"
print(p.lastname)
print(p.name)
