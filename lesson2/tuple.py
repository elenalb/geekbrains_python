# кортежи
# НЕИЗМЕНЯЕМЫЙ
print(tuple('simple string'))
a = (1, 2, 'False', True)
print(a)
print(type(a))

my_list = [1, 2, True]
my_tuple = tuple(my_list)
print(my_tuple)

print(my_list.__sizeof__())
print(my_tuple.__sizeof__())

my_tuple_1 = ([123, 456], 1, True)
print(my_tuple_1)
my_tuple_1[0][0] = 678
print(my_tuple_1)
