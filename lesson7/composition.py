# компощзиция
# len_1 * height, len_2 * height
# S = 2 * (len_1 * height) + 2 * (len_2 * height) = 2 * height * (len_1 + len_2)


class WindowDoor:
    def __init__(self, wd_height, wd_len):
        self.square = wd_len * wd_height


class Room:
    def __init__(self, len_1, len_2, height):
        self.square = 2 * height * (len_1 + len_2)
        self.wd = []

    def add_wd(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_height, wd_len))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(10, 20, 3)
print(r.square)
r.add_wd(2, 1)
r.add_wd(1, 1)
r.add_wd(1, 1)
print(r.common_square())
