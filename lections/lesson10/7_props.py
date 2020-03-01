class A:
    def __init__(self, a):
        self._a = a

    def get_a(self):
        return self._a

    def set_a(self, a):
        self._a = a

    @property
    def a(self):
        return self._a


a = A(100)
print(a.get_a())
print(a.a)
