from secrets import choice
import string
from operator import mul
from random import shuffle, choices, sample
from typing import Counter

# Dataset

one_to_onehundred = [x for x in range(1, 101)] # 1.
print(one_to_onehundred)

two_to_sixty = [x for x in range(1, 61)] # 2.
even = [num for num in two_to_sixty if num % 2 == 0]
print(even)

one_to_seventyseven = [x for x in range(1, 78)] # 3.
odd = [num for num in one_to_seventyseven if num % 2 == 1]
print(odd)

population = list(range(1, 301)) # 4.
#i unique:
hundred_numbers = sample(population, k=100)
print(hundred_numbers)
#ii not unique:
hundred_numbers_2 = (choices(population, k=100))
print(hundred_numbers_2)

color = ["brown", "black", "white", "yellow", "blue"] # 5.
# i.
red_color = ["red"]
red_color.extend(choices(color, k=2))
print(red_color)
# ii.
random_color = choices(red_color, k=50)
print(random_color)
# iii.
print(f'{len(color)} {", ".join(set(color))}')
print(f'{len(red_color)} {", ".join(set(red_color))}')
print(f'{len(random_color)} {", ".join(set(random_color))}')