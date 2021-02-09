# yield

generator_obj = (param ** 2 for param in range(5))

for el in generator_obj:
    print(el)


def generator():
    for el in (1, 2, 3):
        yield el


g = generator()
print(g)

for el in g:
    print(el)
