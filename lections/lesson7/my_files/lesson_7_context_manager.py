import

with open('test_file.txt') as f:
    print(f.readlines())


@contextmanager
def my_open(*args, **kwargs):
    f = open(*args, **kwargs)
    yield f
    f.close


with my_open('test_file.txt', mode='w') as f:
    f.writelines(('!!!!!!!!!!!!!!\n', ))


def cm():
    print('before')
    yield
    print('after')


with cm():
    print('inside')
