class Person:
    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.__salary = salary

    def get_yearly_salary(self):
        return self._salary * 12

p = Person("John", "Doe", 100500)
#print(p.__salary)
print(p._Person__salary)

