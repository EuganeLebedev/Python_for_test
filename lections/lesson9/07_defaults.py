class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        slef.d = None #Хорошая практика инициировать все атрибуты 
                      #при инициализации объекта

    def perimeter(self):
        return (self.a * self.b) *2

    def set_diagonal(self, d):
        self.d = d

rec = Rectangle(10, 5)
rec2 = Rectangle(6, 2)
rec3 = Rectangle(8, 100)

print(rec.perimeter())
print(rec2.perimeter())
print(rec3.perimeter())
