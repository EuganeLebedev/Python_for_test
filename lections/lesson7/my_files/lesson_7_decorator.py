def square(number):
    return number ** 2


def cube(fn):
    def wrapper(number):
        result = fn(number)
        result = result + number

        return result
    
    return wrapper


def square_2(number):
    return number**2

decorated_square = cube(square_2)


@cube
def square(number):
    return number**2


a = 10
b = square(a)

print(b)
