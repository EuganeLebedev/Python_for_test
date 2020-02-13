def test(a, b, c, d, e, f, g):
    print(a, b, c, d, e, f, g)

l = [1,2,3,4,5,6,7]

#test(l[0], l[1], l[2], l[3]...

test(*l)


def test2(*args):
    print(args)

test2(1,2,3,4,5)

test2(*l)


def test3(a, b, *args):
    print(a, b)
    print(args)

test3(1, 2, "qwe", "asd", "adsfsdf")


def test4(a, b, *args, c):
    print(a, b)
    print(args)
    print(c)


test4(1, 2, "weqwe", "qweqwe", c=3)
test4(1,2,c=3)




























