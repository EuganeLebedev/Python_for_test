class Person:

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.__salary = salary


    def get_year_salary(self):
        return self.__salary * 12


p = Person("John", "Doe", "100500")
print(p.get_year_salary())
