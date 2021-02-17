# открытие, закрытие, чтение и запись

# file_obj = open(r"C:\Users\elena.babenko\PycharmProjects\geekbrains_python\lesson5\test_file")

# открытие и чтение
# file = open("test_file", "r")

# read()
# content = file.read()
# print(content)
# file.close()

# readline()
# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)
# file.close()

# readlines()
# lines = file.readlines()
# print(lines)
# file.close()

# считывание файла по частям
# line_list = []
# for line in file:
#     line_list.append(line)
# print(line_list)
# file.close()

# while True:
#     content = file.read(8)
#     print(content)
#
#     if not content:
#         break

# для открытия бинарных файлов: "rb" - read-binary

# запись в файл
# write
# file_to_write = open("file_to_write.txt", "w")
# file_to_write.write("something else")
# file_to_write.close()

# writelines
# file_to_write = open("file_to_write.txt", "w")
# file_to_write.writelines(['str1\n', 'str2\n', 'str3'])
# file_to_write.close()
