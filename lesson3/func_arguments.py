# аргументы

# позиционные и именованные параметры


def first_func(var1, var2, var3):
    return var1 * var2 + var3


# print(first_func(1, 2, 3))


def second_func(var1, var3, var2):
    print(f"var_1 = {var1}, var_2 = {var2}, var_3 = {var3}")


second_func(1, 3, 2)

# обязательные и необязательные


def first_func(var1, var2, var3):
    return var1 * var2 + var3


def second_func(var1, var2=2, var3=3):
    return var1 * var2 + var3


# print(second_func(1, var3=4))


# args / kwargs

def my_func(*args):
    return args


print(my_func(1, 4, 'string', ['list', 1]))


# kwargs = key-word arguments

def my_kword_func(**kwargs):
    return kwargs


print(my_kword_func(var_1=1, var_2='str', var_3=[1, 3]))
