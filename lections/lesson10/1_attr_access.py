class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"A: a={self.a}, b={self.b}"

a = A(1,2,3)


print(a.__dict__)
print(a)

