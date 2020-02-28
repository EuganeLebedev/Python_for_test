import json

def my_func_decor(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(args, '\n', kwargs)
        return result

    return wrapper


@my_func_decor
def my_func(a=1, b=2, c=5, **kwargs):
    print('Inside my func')


def main():
    my_func(1, 2, 3, z=1, x=2, v=13)
    with open('../../../test.txt', 'w') as file:
        #file = open('test.txt', 'w')
        file.write(json.dumps(my_func(1, 2, 3)))
        #file.close()



main()
