from functools import reduce

def my_func(array):
    if len(array) > 0:
        return reduce(lambda a, x: a + 1 if x else a+0, array)
    else:
        return 0

array1 = [];
print(len(array1))
print(my_func(array1))