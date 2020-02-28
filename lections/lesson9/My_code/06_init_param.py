class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a * self.b) *2

rec = Rectangle(10, 5)
rec2 = Rectangle(6, 2)
rec3 = Rectangle(8, 100)

print(rec.perimeter())
print(rec2.perimeter())
print(rec3.perimeter())
