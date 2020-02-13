def test():
    print("enter test")

    def inner_func():
        print("inner")

    print("exit test")

    return inner_func


inner = test()

inner()


def hoc(fn):
    print("before")
    fn()
    print("after")


def fn_arg():
    print("test")


hoc(fn_arg)


hoc(lambda: print(1))























