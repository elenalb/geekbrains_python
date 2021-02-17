# менеджер контекста

# file = open("path_to_file")
# file.read()
# file.close()

with open("test_file") as file:
    for line in file:
        print(line)
