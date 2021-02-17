# указатель в файле

file = open("test_file")
content1 = file.read()
print(content1)
print(f"Указатель находится на {file.tell()} позиции")
# file.close()

# seek() - перенос указателя
file.seek(0)
print(f"Указатель теперь находится на {file.tell()} позиции")
content2 = file.read()
print(content2)

file.close()
