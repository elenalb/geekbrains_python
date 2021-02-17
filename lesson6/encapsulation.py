# инкапсуляция


class MyClass:
    _protected_param = "hello"
    __private_param = "hello1"

    def _protected_method(self):
        print("Это защищенный метод!")

    def __private_method(self):
        print("Это приватный метод!")


mycl = MyClass()
mycl._MyClass__private_method()
print(mycl._MyClass__private_param)
