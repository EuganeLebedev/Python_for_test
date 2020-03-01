class A:

    c = 100

    def __init__(self, c):
        self.c = c

    @classmethod
    def cm(cls):
        cls.c = 10050000000

a = A(1)
b = A(2)

print(a.c)
print(b.c)

del a.c

print(a.c)
print(b.c)
