def test(a, b, /, c, *, d):
    print(a, b, c)

#test(a=1, b=2, c=3, d=6)

test(1, 2, 3, d=6)
test(1,2, c=3, d=6)
