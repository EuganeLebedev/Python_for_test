import shutil
from contextlib import contextmanager

#with open("test.txt") as f:
#    print(f.readlines())

@contextmanager
def my_open(*args, **kwargs):
    f = open(*args, **kwargs)
    yield f
    f.close()

with my_open("test.txt", mode="w") as f:
    f.writelines(("!!!!!!!!!!\n", ))

@contextmanager
def cm():
    print("before")
    yield
    print("after")

with cm():
    print("inside")


shutil.copyfile("test.txt", "new_test.txt")
