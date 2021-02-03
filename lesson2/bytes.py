# byte

print(b'text')
print('текст'.encode())

byte_txt = 'текст'.encode()
print(byte_txt)
str_txt = byte_txt.decode()
print(str_txt)
print(type(byte_txt))

# bytearray
my_byte_array = bytearray(b'text')
print(my_byte_array)
print(type(my_byte_array))
