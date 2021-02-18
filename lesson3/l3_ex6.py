"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    try:
        return word.capitalize()
    except AttributeError:
        print("В функцию необходимо передать строку!")


def extended_int_func(sequence):
    # str.title() - самый простой способ!
    words_list = sequence.split()
    for ind, word in enumerate(words_list):
        words_list[ind] = int_func(word)
    return ' '.join(words_list)


print(int_func('hello'))
print(extended_int_func('hello my name is python'))
