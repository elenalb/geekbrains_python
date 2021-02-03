# тернарный оператор

# condition_if_true if condition else condition_if_false

digit = 'четное' if 10 % 2 == 0 else 'нечетное'
print(digit)

# условия с кортежами
# (condition_if_false, condition_if_true)[condition]
new_digit = ('нечетное', 'четное')[10 % 2 == 0]
print(new_digit)

my_var_1 = True or 'something'
my_var_2 = False or 'something'

print(my_var_1)
print(my_var_2)

function_return = None

message = function_return or "Функция ничего не вернула"

print(message)
