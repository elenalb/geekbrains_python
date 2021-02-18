# интерфейсы
# abc - Abstract Base Classes - встроенный модуль

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def my_method1(self):
        pass

    @abstractmethod
    def my_method2(self):
        pass


class MyClass(MyAbstractClass):
    def my_method1(self):
        print("Метод my_method1()")

    def my_method2(self):
        print("Метод my_method2()")


mc = MyClass()
mc.my_method1()
