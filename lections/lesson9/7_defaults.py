class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        self.d = None

    def perimeter(self):
        return (self.a + self.b) * 2

rec = Rectangle(10, 5)
rec2 = Rectangle(6, 3)
rec3 = Rectangle(100, 534)

print(rec.perimeter())
print(rec2.perimeter())
print(rec3.perimeter())

