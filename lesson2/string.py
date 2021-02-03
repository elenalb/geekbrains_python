# string
my_str_1 = str("simple string")
my_str_2 = "second string"

# конкатенация
string_sum = my_str_1 + " " + my_str_2
print(string_sum)

# взятие элемента по индексу
# print(string_sum[0])

# срезы! [s:f:step]; s - начало отсчета, f - конец отсчета, step - шаг
# print(string_sum[3:6])
# print(string_sum[3:-3])
# print(string_sum[:10])
# print(string_sum[6:])
# print(string_sum[:])
# print(string_sum[::-1])
# print(string_sum[1:7:2])

# реверс строк
# 1. срез с конца
print(string_sum[::-1])

# 2. обратная итерация
for el in reversed(string_sum):
    print(el, end="")

# 3. реверс на месте
reversed_str = ""
symbols = list(string_sum)
for el in range(len(string_sum) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(string_sum) - el - 1]
    symbols[len(string_sum) - el - 1] = tmp
reversed_str = "".join(symbols)
print(reversed_str)

# методы
print(len(string_sum))
print(string_sum.split(' '))
string_upper = string_sum.upper()
print(string_upper)
string_lower = string_upper.lower()
print(string_lower)


