class A:

    c = 100

    @classmethod
    def cm(cls):
        cls.c = 10050000000

a = A()
b = A()

print(a.c)
print(b.c)

A.cm()

print(a.c)
print(b.c)

