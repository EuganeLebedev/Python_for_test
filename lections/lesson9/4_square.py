class Square:

    def set_side(self, side):
        self.side = side

    def square(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 4

sq1 = Square()
sq1.set_side(10)
print(sq1.square())
print(sq1.perimeter())
