# class - класс


# наименование класса с большой буквы - CamelCase
class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def on_auto_start(self, auto_name, auto_year):
        print("Заводим автомобиль")
        # атрибуты экземпляра
        self.auto_name = auto_name
        self.auto_year = auto_year
        Auto.auto_count += 1

    def on_auto_stop(self):
        print("Останавливаем автомобиль")


# auto = Auto()  # объект класса Auto
# print(auto)
# auto.on_auto_start("Audi", 2010)
# print(auto.auto_name)
# print(auto.auto_year)
# print(auto.auto_count)

auto_2 = Auto()
auto_2.on_auto_start("Mazda", 2000)
print(auto_2.auto_name)
print(auto_2.auto_count)
