# импорт из стандартной библиотеки

import time
import random

time.time()
random.random()

from time import time

time()

import my_functions

my_functions.show_message()
print(my_functions.summa())

from my_functions import show_message

show_message()
