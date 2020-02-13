def test(a, b, c):
    print(a, b, c)

d = {
    "a": 100,
    "b": 300,
    "c": 500,
}

test(a=1, b=2, c=3)

test(**d)

def test2(a, b, c, d):
    print(a)
    print(b, c, d)

d2 = {
    "d": 100,
    "b": 300,
    "c": 500,
}

test2(1, **d2)


def test3(a, b, **kwargs):
    print(a, b)
    print(kwargs)

test3(1, 2, c=3, d=5, f=100)



def test4(y, *args, **kwargs):
    print(y)
    print(args)
    print(kwargs)

    print(kwargs["c"])


test4(1,2,3,4,5, a=1000, b=3345, c=3453)













