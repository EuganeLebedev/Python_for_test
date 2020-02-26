class Person:

    def __init__(self, name):
        self.name = name

#Метод отработает, есди нет атрибута у объекта
#Без переопределения выскакивает ошибка
#В начале выполняется __getattribute__
#Есди ничего не найдено, то вызввается __getattr__
    def __getattr__(self, attr):
        return "NON EXISTING"



p1 = Person("Ivan")

print(p1.lastname)
