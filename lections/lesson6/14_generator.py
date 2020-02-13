def odd_range(n):
    value = 2

    while value < n:
        yield value
        value += 2


for i in odd_range(10):
    print(i)


a = (x**2 for x in odd_range(10))

