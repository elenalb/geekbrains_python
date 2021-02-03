# объединение списков без цикла

my_list_1 = [[1, 2], [3, 4], [5, 6]]
print(sum(my_list_1, []))

# поиск уникальных элементов
my_list_2 = [1, 4, 4, 5, 3, 5, 1, 4]
print(list(set(my_list_2)))

# обмен значениями через кортежи
var_1, var_2 = 1, 2
print(var_1, var_2)

var_1, var_2 = var_2, var_1
print(var_1, var_2)

# вывод несуществующего значения ключа
my_dict = {1: 1, 2: 2}
print(my_dict[1])
print(my_dict.get(5))

# поиск самых часто встречающихся элементов списка
my_list_3 = [1, 4, 4, 5, 3, 5, 1, 4]
print(max(set(my_list_3), key=my_list_3.count))

# распаковка последовательностей с помощью *
my_list_4 = [56, 2, 5, 323, 66, 765]
*el_1, el_2, el_3 = my_list_4
print(el_1)
print(el_2)
print(el_3)
el_1, *el_2, el_3 = my_list_4
print(el_1)
print(el_2)
print(el_3)

# вывод print() без перевода строки
# for el in my_list_4:
#     print(el, end=' ')

# сортировка словаря по значениям
my_dict_1 = {'python': 1991, 'java': 1995, 'c++': 1987}
print(sorted(my_dict_1))

print(sorted(my_dict_1, key=my_dict_1.get))

# нумерованные списки
for ind, el in enumerate(my_list_4):
    print(ind, el)

# транспонирование матрицы
# 1 2 4
# 4 5 6
# 6 7 8

# 1 4 6
# 2 5 7
# 4 6 8

# a b
# c d
# e f

old_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
new_list = zip(*old_list)

# a c e
# b d f

print(list(new_list))
