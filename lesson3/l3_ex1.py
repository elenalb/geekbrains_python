"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_func(numerator, denominator):
    try:
        result = numerator / denominator
        print(f"{numerator} / {denominator} = {result}")
        return result
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")


try:
    numerator_input = int(input("Введите числитель: "))
    denominator_input = int(input("Введите числитель: "))

    division_func(numerator_input, denominator_input)
except ValueError:
    print("Нужно было ввести числа!")
