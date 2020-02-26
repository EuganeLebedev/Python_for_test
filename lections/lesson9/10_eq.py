class Person:

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self._salary = salary


    def get_year_salary(self):
        return self._salary * 12

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        return self.name + other.name

p1 = Person("John", "Doe", "100500")
p2 = Person("Ivan", "Ivanov", "100400")
p3 = Person("John", "Doe", "100500")

print(p1 == p2)
"""
Объекты сравниваются по id
Переопределение логики сравнения через __eq__
"""
print(p1 == p3)
