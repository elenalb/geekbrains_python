# обработка ошибок

try:
    with open("test_file") as file:
        for line in file:
            print(line)
except IOError:
    print("IOError - smth wrong with file")
