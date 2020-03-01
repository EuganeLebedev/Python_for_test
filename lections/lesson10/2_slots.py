class A:

    __slots__ = ("a", "b", "c")

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        return f"A: a={self.a}, b={self.b}"

a = A(1,2,3)


print(a)

a.qwe = 100

