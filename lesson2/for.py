# цикл for in

for el in "string":
    print(el)

my_tuple = (1, 2, 3)
my_list = []
for el in my_tuple:
    my_list.append(el)

print(my_tuple)
print(my_list)

for el in my_list:
    print(el**2)

my_dict = {'lesson1': 'basics', 'lesson2': 'types'}

for key, value in my_dict.items():
    print(key, value)

for key in my_dict.keys():
    print(key)
