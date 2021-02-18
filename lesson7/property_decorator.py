# декоратор @property


class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    @property
    def my_method(self):
        return f"Параметры класса: {self.param1}, {self.param2}"


mc = MyClass("param1", "param2")
# print(mc.param1)
# print(mc.param1)
#
print(mc.my_method)
print(type(mc.my_method))


# 2000-2019 гг
class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Год выпуска автомобиля - {self.year}"

#
# a = Auto(2000)
# print(a.get_auto_year())
