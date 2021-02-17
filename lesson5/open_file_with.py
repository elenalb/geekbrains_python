# режимы доступа
# r - чтение
# w - запись. Если файл не сущ - создает файл, если сущ - перезаписывает
# x - запись. Если файла не сущ - создает файл, если сущ - ошибка
# a - дозапись. Добавление информации в конец файла.
# b - открыть файл в бинарном формате
# t - открыть файл в текстовом формате
# + - открыть файл на чтение и запись

# режим x vs режим w
# file_1 = open("my_file", "w")
# file_2 = open("my_file", "x")  # не может открыть уже существующий файл!

# file_1.close()
# file_2.close()

# режим append
# file_to_append = open("test_file", "a")
# file_to_append.write("something to write!")
# file_to_append.close()

# режим b
# bin_file = open("bin_file", "wb")
# bin_file.write(b"if5s")
# bin_file.close()

# режим +
with open("my_file", "r+") as file:
    file.write("something else!")
    print(file.tell())
    file.seek(0)
    content = file.read()  # !!! не забываем переместить указатель на начало!
    print(content)
    file.close()

# параметры файлового объекта

# file.closed
# file.mode
# file.name

# with open("test_file") as file:
#     print(file.mode)
#     print(file.name)
#     for line in file:
#         print(line)
#
# print(file.closed)
