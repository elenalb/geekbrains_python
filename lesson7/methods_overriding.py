# переопределние методов


class ParentClass:
    def __init__(self):
        print("Конструктор класса-родителя ParentClass")

    def my_method(self):
        print("Метод my_method() класса-родителя")


class ChildClass(ParentClass):
    def __init__(self):
        print("Конструктор класса-потомка ChildClass")
        # ParentClass.__init__(self)  # эквивалентный способ
        super().__init__()

    def my_method(self):
        print("Метод my_method() класса-потомка")
        # ParentClass.my_method(self)  # эквивалентный способ
        super().my_method()


c = ChildClass()
c.my_method()
