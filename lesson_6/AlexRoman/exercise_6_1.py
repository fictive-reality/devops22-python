# `Exercise 1` Dataset

# Todays exercises requires that you generate test data. You can generate data in multiple ways i.e 
# manually through loops, using `random` module or list comprehension. See examples in `8_data.py`.

# 1. Generate a list containing the numbers 1, 2, 3 to 100.
# 2. Generate a list of all even numbers from 2 to 60
# 3. Generate a list of all odd numbers from 1 to 77
# 4. Generate a list of 100 numbers between 1 - 300
#     1. The numbers must be unique
#     2. The numbers are selected randomly (not unique)
# 5. create a list containing five colors (not containing red)
#    1. Create a new list containing "red" and also add two colors by random with `choice`, `choices` or `sample` from the list.
#    2. Generate a list of random colors from the list of 3, the list should be of length 50.
#    3. Print the length of all three lists and the unique colors in each list

import random
from random import shuffle, choices, sample


numbers = []
even_numbers = []
odd_numbers = []
separation = "==================================================="

for x in range(100):
    numbers.append(x)
print(f"1. The numbers from 0 to 100: {numbers}")
print(separation)

for x in range(2, 61,):
    if x % 2 == 0:
        even_numbers.append(x)
print(f"2. Variant 1. (With modulo) The even numbers from 2 to 60 are: {even_numbers}")
print(separation)

even_2 = []
for x in range(2, 61, 2):
    even_2.append(x)
print(f"2. Variant 2. (Wirh steps in range) The even numbers from 2 to 60 are: {even_2}")
print(separation)

for x in range(1, 78):
    if x% 2 != 0:
        odd_numbers.append(x)
print(f"3. The odd numbers from 1 to 77 are: {odd_numbers}")
print(separation)

random_100_list = random.sample(range(0, 300), 100)
unique_list = set(random.sample(range(0, 300), 100))

print(f"4.1 Unique list and sorted: {unique_list}")
print(f"The lenght of the unique list is {len(unique_list)}")
print(separation)

print(f"4.2 The unsorted random list: {random_100_list}")
print(f"The lenght of the random list is {len(random_100_list)}")
print(separation)

colors = ["black", "yellow", "blue", "green", "purple"]
second_colors = ["red"]
extended = random.choices(colors, weights=None, cum_weights=None, k=2)
second_colors_extended = second_colors + extended
print(f"5. The color list:{colors}")
print(separation)
print(f"5.1 The second list:{second_colors}")
print(separation)
print(f"The second list extended:{second_colors_extended}")
print(separation)
long_list = random.choices(second_colors_extended, k = 50)

print(f"5.2 The super extended list (50): {long_list}")
print(separation)

print(f"5.3 The lenght of the color list is {len(colors)} and contains this unique elements: {set(colors)}")
print(separation)
print(f"5.3 The lenght of the second list extended is {len(second_colors_extended)} and contains this unique elements: {set(second_colors_extended)}")
print(separation)
print(f"5.3 The lenght of the super extended list is {len(long_list)} and contains this unique elements: {set(long_list)}")
print(separation)





        