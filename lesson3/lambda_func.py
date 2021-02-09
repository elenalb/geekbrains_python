# анонимные lambda функции

my_func = lambda var_1, var_2: var_1 + var_2

print(my_func(2, 5))
print(my_func('hello, ', 'world'))

print((lambda var_1, var_2: var_1 + var_2)(2, 5))
print((lambda var_1, var_2: var_1 + var_2)('hello, ', 'world'))
