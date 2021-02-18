# интерфейс итерации

my_list = [10, 12, "test", True]
# for el in my_list:
#     print(el)

# 1. __iter__() для my_list - возвращает объект с методом __next__()
# 2. for in запускает __next__()
# 3. Когда элементы закончились, __next__() генерирует исключение StopIteration
# for in перехватывает это исключение и завершает свою работу

# создаем собственный итератор


class Iterator:
    """
    Объект-итератор
    """
    def __init__(self, start=0):
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class IterObj:
    """
    Объект, который поддерживает интерфейс итерации
    """
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        # __iter__() должен возвращать объект-итератор
        return Iterator(self.start)


obj = IterObj(start=1)
# for el in obj:
#     print(el)


class Iter:
    def __init__(self, start=0):
        self.start = start
        self.i = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            self.i = self.start - 1
            raise StopIteration


obj_iter = Iter(start=3)
for el in obj_iter:
    print(el)

for el in obj_iter:
    print(el)
