# functools

# reduce()

from functools import reduce


def my_func(el1, el2):
    return el1 + el2


print(reduce(my_func, [1, 2, 3]))

# partial()

from functools import partial

new_my_func = partial(my_func, 10)
print(new_my_func)
print(new_my_func(10))


def my_func_1(el1, el2, el3):
    return el1 + el2 ** el3


partial_my_func = partial(my_func_1, el1=10, el3=2)
print(partial_my_func(el2=10))
