# наследование

# класс, наследующий характеристики другого класса - дочерний
# класс, предоставляющий свои характеристики - родительский


# родительский класс
class Transport:
    transport_attr = "Атрибут класса Transport"
    _protected_param = "Protected param"
    __private_param = "Private param"

    def transport_method(self):
        print("Это родительский класс Transport!")


# дочерний класс
class Auto(Transport):
    def auto_method(self):
        print("Это дочерний класс Auto!")


# a = Auto()
# a.transport_method()
# a.auto_method()
# print(a.transport_attr)

# 1. Несколько дочерних классов у одного родителя

# Второй дочерний класс
class Bus(Transport):
    def bus_method(self):
        print("Это дочерний класс Bus!")


class Bus2(Bus):
    def second_bus_method(self):
        print("Это дочерний класс Bus2")


# b2 = Bus2()
# print(b2.transport_attr)
# print(b2._protected_param)
# print(b2._Bus2__private_param)  # виден только внутри класса, в котором определен
# print(b2._Transport__private_param)  # получаем доступ с именем родительского класса,
# в котором объявлен приватный атрибут

# a = Auto()
# b = Bus()
# a.transport_method()
# b.transport_method()

# Несколько родителей


# Первый родитель
class Player:
    def player_method(self):
        print("Родительский класс Player")


# Второй родитель
class Navigator:
    def navigator_method(self):
        print("Родительский класс Navigator")


# Дочерний класс
class MobilePhone(Player, Navigator):
    def mobile_phone_method(self):
        print("Это дочерний класс MobilePhone")


# m_p = MobilePhone()
# m_p.player_method()
# m_p.navigator_method()
# m_p.mobile_phone_method()


# совпадение имен атрибутов и методов
class Shape:
    def __init__(self, param_1, param_2):
        print("Shape.__init__")
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Shape: {self.param_1}, {self.param_2}"

    def shape_method(self):
        print("Shape method!")


class Material:
    def __init__(self, param_1, param_2):
        print("Material.__init__")
        self.param_1 = param_1
        self.param_2 = param_2

    def get_params(self):
        return f"Параметры Material: {self.param_1}, {self.param_2}"


class Triangle(Material, Shape):
    def __init__(self, param_1, param_2):
        super().__init__(param_1, param_2)  # для работы с наследованными атрибутами
        pass


# t = Triangle(1, 2)
# print(t.get_params())
# t.shape_method()
