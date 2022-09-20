import string
from operator import mul
from random import shuffle, choices, sample
from typing import Counter

# for loop

data_with_loop = []

for i in range(5):
    for val in ["yellow", "blue", "green"]:
        data_with_loop.append(val)

print(data_with_loop)

five_of_each = ["yellow", "blue", "green"] * 5
print(five_of_each)

five_of_each_sorted = sorted(five_of_each)
print(five_of_each_sorted)

# List comprehension, 1 to 10

one_to_ten = [x for x in range(1, 11)]
print(one_to_ten)

# power of two
power_of_two = [2**x for x in range(0, 10)]
print(power_of_two)

# https://docs.python.org/3/library/random.html#functions-for-sequences

pick_ten = choices(["Dog", "Cat", "Bird"], k=10)
print(pick_ten)

pick_ten_favor_dog = choices(["Dog", "Cat", "Bird"], weights=[10, 1, 1], k=10)
print(pick_ten_favor_dog)


# Random shuffle
# https://docs.python.org/3/library/random.html#random.shuffle


names = ["Adam", "Bertil", "Caesar", "David", "Erik",
         "Filip", "Gustav", "Helge", "Ivar", "Johan"]

# Shuffle will change the order in place
shuffle(names)
print(names)

# If you want a new list use sample, this will make 10 of each
sample_names = sample(names, counts=[10]*10, k=100)
print(sample_names)
print(Counter(sample_names).most_common())


# If you want it to be random the population must be larger than the k value
large_name_population = names * 100
sample_names = sample(large_name_population, k=100)
print(Counter(sample_names).most_common())

# You can increase the population with the counts argument
sample_names = sample(names, counts=[50]*len(names), k=100)
print(Counter(sample_names).most_common())

# https://docs.python.org/3/library/string.html#string.ascii_uppercase
# Generate A-Z
print(list(string.ascii_uppercase))

abc = list(string.ascii_uppercase)
