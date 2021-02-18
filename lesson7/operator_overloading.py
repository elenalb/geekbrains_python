# перегрузка операторов

# __init__()
# __del__()
# __str__()
# __add__()


class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    # def __del__(self):
    #     print(f"Удаляем объект {self.param1} класса MyClass")

    def __str__(self):
        return f"Объект с параметрами {self.param1}, {self.param2}"

    def __add__(self, other_param):
        return MyClass(self.param1 + other_param.param1, self.param2 + other_param.param2)


mc_1 = MyClass(1, 2)
mc_2 = MyClass(2, 3)
print(mc_1 + mc_2)
# print(mc.param)
# del mc
# print(mc)

# __getitem__()


class Class1:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return str(self.param)


class Class2:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))


my_obj = Class2(10, True, "text")
print(my_obj.my_list[1])


class Class2Modified:
    def __init__(self, *args):
        self.my_list = []
        for el in args:
            self.my_list.append(Class1(el))

    def __getitem__(self, index):
        return self.my_list[index]


my_obj_modified = Class2Modified(10, True, "text")
print(my_obj_modified.my_list[0])
print(my_obj_modified[0])
