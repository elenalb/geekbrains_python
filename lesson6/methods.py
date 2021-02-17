# методы класса
# модификаторы доступа:
# 1 - public - можно менять за пределами класса
# 2 - protected - _protected_var_name - значение можно менять только в пределах одного пакета
# 3 - private - __private_var_name - значение можно менять только в пределах класса


class Auto:
    info_1 = "Класс Auto"

    def __init__(self):
        print(Auto.info_1)
        self.auto_name = "Audi"
        self._auto_year = 2010
        self.__auto_model = "Cd24"

    def get_class_info(self):
        print("Детальная информация о классе Auto")

    def on_start(self):
        info_2 = "Автомобиль заводится"
        return info_2


a = Auto()
print(a.auto_name)
# print(a._auto_year)
# print(a.__auto_model)  # вызов не работает!
