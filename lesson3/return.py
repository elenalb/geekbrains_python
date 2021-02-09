# return

# return со значением


def s_calc():
    rad = int(input("Введите радиус цилиндра: "))
    h = int(input("Введите высоту цилиндра: "))
    # площадь основания
    s_circle = 3.14 * rad ** 2
    # площадь боковой поверхности
    s_side = 2 * 3.14 * rad * h
    # площадь поверхности цилиндра
    s = s_circle * 2 + s_side
    return s


# return без значения


def s_calc_empty_return():
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


# return набора значений


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
    return s, rad, h


func_return = s_calc_several_values()
print(func_return)

s, rad, h = func_return
# s, rad, h = s_calc_several_values()
print(s, rad, h)

s_circle = rad ** 2 * 3.14
