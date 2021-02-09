"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number = int(input('Введите целое положительное число: '))
largest_num = 0
while number > 0:
    remain = number % 10
    if remain > largest_num:
        largest_num = remain
    number //= 10
print(largest_num)
