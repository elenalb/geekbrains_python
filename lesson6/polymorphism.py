# полиморфизм


# перегрузка методов
class Auto:
    def auto_start(self, param_1, param_2=None):
        if param_2:
            print(f"Сумма параметров = {param_1 + param_2}")
        else:
            print(f"Param_1 = {param_1}")


# a = Auto()
# a.auto_start(50)
# a.auto_start(10, 10)


# переопределение методов
class Transport:
    def show_info(self):
        print("Родительский класс Trandport")


class Moto(Transport):
    def show_info(self):
        print("Метод класса Moto")


class Bus(Transport):
    def show_info(self):
        print("Метод класса Bus")


t = Transport()
t.show_info()

m = Moto()
m.show_info()

b = Bus()
b.show_info()
