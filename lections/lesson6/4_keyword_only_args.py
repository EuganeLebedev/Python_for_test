def test(a, b, *, c):
    print(a, b, c)

try:
    test(1, 2, 3)
except TypeError:
    print("нельзя")

test(1, 2, c=3)



