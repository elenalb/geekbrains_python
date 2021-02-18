"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и
возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    args_list = [a, b, c]
    args_list.remove(min(args_list))
    return sum(args_list)


max_sum = my_func(1, -1, 4)
print(max_sum)
