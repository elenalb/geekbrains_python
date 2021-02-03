# словарь
my_dict_1 = dict(key_1=1, key_2=2)
my_dict_2 = {3: '3', 4: '4'}

print(my_dict_2)

print(my_dict_2.keys())
print(my_dict_2.values())
print(my_dict_2.items())

print(my_dict_2.get(3))
print(my_dict_2.get(6))
my_dict_2.update({5: '5'})
print(my_dict_2)

my_dict_3 = my_dict_2.copy()
print(my_dict_3)
print(my_dict_3 is my_dict_1)

my_dict_3.clear()
print(my_dict_3)

