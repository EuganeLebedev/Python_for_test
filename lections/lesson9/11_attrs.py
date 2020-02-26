class Person:

    def __init__(self, name):
        self.name = name

    def __getattribute__(self, attr):
        print(f"getattribute: attr={attr}")
        inner_dict = object.__getattribute__(self, "__dict__")
        #Получение аттрибута минуя магический метод. ИНаче рекурсия
        return inner_dict[attr]


p1 = Person("Ivan")

print(p1.name)
