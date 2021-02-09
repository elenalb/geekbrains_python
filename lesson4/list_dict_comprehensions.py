# генераторы списков и словарей

# lists
my_list = [1, 2, 3, 4, 5]
new_list = []
for i in my_list:
    new_list.append(i**2)

new_list_comp = [el**2 for el in my_list]

lines = [line.strip() for line in open("text.txt")]

new_list_1 = [el for el in my_list if el % 2 == 0]

str_1 = 'abc'
str_2 = 'def'
str_3 = 'gh'

new_list_2 = [i+j+k for i in str_1 for j in str_2 for k in str_3]

# словари и множества
my_set = {el**2 for el in range(10)}

my_dict = {el: el**2 for el in range(5)}
print(my_dict)

my_list_of_floats = [2.4324324, 5.3243234, 6.23424]

new_list_round = [round(el, 2) for el in my_list_of_floats]
print(new_list_round)
