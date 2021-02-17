# конструкторы и методы


class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def __init__(self):
        Auto.auto_count += 1
        print(Auto.auto_count)


a_1 = Auto()
a_2 = Auto()
a_3 = Auto()
