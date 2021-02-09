# области видимости

# local


def s_calc_several_values():
    try:
        rad = int(input("Введите радиус цилиндра: "))
        h = int(input("Введите высоту цилиндра: "))
    except ValueError:
        return
    # площадь основания
    s_circle = 3.14 * rad ** 2
    # площадь боковой поверхности
    s_side = 2 * 3.14 * rad * h
    # площадь поверхности цилиндра
    s = s_circle * 2 + s_side
    return s


# global

rad = None
h = None
s_circle = None
s_side = None


def s_calc_several_values_global():
    global rad, h, s_circle, s_side
    try:
        rad = int(input("Введите радиус цилиндра: "))
        h = int(input("Введите высоту цилиндра: "))
    except ValueError:
        return
    # площадь основания
    s_circle = 3.14 * rad ** 2
    # площадь боковой поверхности
    s_side = 2 * 3.14 * rad * h
    # площадь поверхности цилиндра
    s = s_circle * 2 + s_side
    return s


# my_func = s_calc_several_values_global()


# nonlocal
def first_func():
    my_var = 0

    def second_func():
        def third_func():
            nonlocal my_var
            my_var += 1
            return my_var
        return third_func()
    return second_func()


my_func_1 = first_func()
print(my_func_1)
