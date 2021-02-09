# named functions


def my_sum(arg1, arg2):
    return arg1 + arg2


def first_func(arg1):
    def second_func(arg2):
        return arg1 * arg2
    return second_func


def func_to_write():
    pass


print(func_to_write())
