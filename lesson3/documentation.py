# документирование функций

# однострочная документация


def is_odd(digit):
    """Показывает, является ли нечетным число"""
    if digit % 2 == 1:
        return True
    return False


# многострочная документация


def is_odd(digit):
    """
    Показывает, является ли нечетным число

    :param digit: int
    :return: bool
    """
    if digit % 2 == 1:
        return True
    return False
