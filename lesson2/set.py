# множества
my_set_1 = set('simple')
my_set_2 = frozenset('simple')
print(my_set_1)
print(my_set_2)
my_set_1.add(1)
print(my_set_1)
my_set_1.remove('s')
print(my_set_1)
my_set_1.pop()
print(my_set_1)

my_set_3 = {1, 3}
print(my_set_3)

my_set_3.clear()
print(my_set_3)

print(my_set_1)
print(my_set_2)

# вычитание
print(my_set_2 - my_set_1)

# объединение
print(my_set_1 | my_set_2)

my_set_1 = set('simple')
my_set_2 = frozenset('simple')
my_set_4 = set('and')
print(my_set_1 - my_set_4)
