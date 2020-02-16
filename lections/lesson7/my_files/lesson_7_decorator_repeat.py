#! /usr/bin/env python3

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        print('hello from wrapper')
        result = fn(*args, **kwargs)
        return result

    return wrapper


@my_decorator
def my_func(a, b, *args, **kwargs):
    print('my function')
    print(a, b)
    print(args)
    print(kwargs)
    return True

@my_decorator
def test():
    print('Test')

my_func(1, 2, 3, 4, 5, 6, 7, 8, c=9, d=10)

test()
