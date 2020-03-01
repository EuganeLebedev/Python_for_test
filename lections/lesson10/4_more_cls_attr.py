class A:

    c = 100

    @classmethod
    def cm(cls):
        return 1

a = A()
b = A()

print(a.c)
print(b.c)

a.c = 100500

print(a.c)
print(b.c)
