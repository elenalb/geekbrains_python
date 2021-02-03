# list - списки
my_list_1 = [1, 2, 'string', False]
my_list_2 = list('simple string')

print(my_list_1)
print(my_list_2)

# изменяемый тип данных!
my_list_1[0] = 10
print(my_list_1)

# методы списков
my_list_1.append('new string')
print(my_list_1)
my_list_1.extend([6, 7])
print(my_list_1)
my_list_1.insert(3, True)
print(my_list_1)
my_list_1.remove(True)
print(my_list_1)
my_list_1.pop(4)
print(my_list_1)

my_list_1.extend([1, 1, 1])
print(my_list_1)
my_list_1.remove(1)
print(my_list_1)

# операторы is и in
print((False and 1) in my_list_1)

my_list_3 = my_list_1
print(my_list_1 is my_list_3)
print(my_list_3)
my_list_1.remove(10)
print(my_list_3)

# shallow copy
copy_list = my_list_1.copy()
print(copy_list)
print(copy_list is my_list_1)
print(copy_list[0] is my_list_1[0])
