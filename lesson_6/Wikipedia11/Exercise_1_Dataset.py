# Generate a list containing the numbers 1, 2, 3 to 100.
# Generate a list of all even numbers from 2 to 60
# Generate a list of all odd numbers from 1 to 77
# Generate a list of 100 numbers between 1 - 300
# The numbers must be unique
# The numbers are selected randomly (not unique)
# create a list containing five colors (not containing red)
# Create a new list containing "red" and also add two colors by random with choice, choices or sample from the list.
# Generate a list of random colors from the list of 3, the list should be of length 50.
# Print the length of all three lists and the unique colors in each list

from asyncio import coroutines
from enum import unique
import random
from collections import Counter
import collections
from random import sample
"""
# ------------------------------------EXERCISE 1------------------------------------

one_to_hundred = [x for x in range(1, 101)]
print(one_to_hundred)

# ------------------------------------EXERCISE 2------------------------------------

one_to_hundred_even = [x for x in range(2, 61, 2)]
print(one_to_hundred_even)

# ------------------------------------EXERCISE 3------------------------------------

one_to_77 = [x for x in range(1, 78, 2)]
print(one_to_77)
"""
# ------------------------------------EXERCISE 4------------------------------------
# the code works.
# I had to create a second list to store the not unique values.
# because the first list is only supposed to store unique values.
# So the loop checks if the value already is in the first list,
# if it is then it stores it in second list, if not it stores it in
# the first list
"""
random_num_100_shit = []
random_num_100 = []
while len(random_num_100) != 100:
    random_num = random.randint(1, 301)
    if random_num in random_num_100:
        random_num_100_shit.append(random_num)
    elif random_num != random_num_100:
        random_num_100.append(random_num)
else:
    print(random_num_100)
"""
# ------------------------------------EXERCISE 5------------------------------------

colors = ["green", "yellow", "blue", "black", "white"]

red_list = ["red"]

red_list.extend(random.choices(colors, k=2))

random_colors = random.choices(red_list, k=50)

print(len(colors))
print(set(colors))

print(len(red_list))
print(set(red_list))

print(len(random_colors))
print(set(random_colors))