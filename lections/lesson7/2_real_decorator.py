from time import time
from functools import wraps

def time_me(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()

        result = fn(*args, **kwargs)

        stop = time()

        delta = stop - start

        print("Time: ", delta)

        return result

    return wrapper

@time_me
def powfn(m, n):
    return m ** n
