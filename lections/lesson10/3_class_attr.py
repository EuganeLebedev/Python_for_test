class A:

    b = None
    c = 100

    @classmethod
    def cm(cls):
        return 1

a = A()

print(a.b)
print(a.c)
print(A.cm())
print(a.cm())

