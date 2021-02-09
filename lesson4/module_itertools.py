# itertools

# count()

from itertools import count

for el in count(10):
    # print(el)
    if el > 15:
        break

# cycle()

from itertools import cycle

c = 0
for el in cycle("abc"):
    if c > 5:
        break
    # print(el)
    c += 1

fruits = ['apple', 'orange', 'kiwi']
iter = cycle(fruits)
print(iter)

iter_1 = cycle(fruits)
print(iter_1)

print(next(iter))
