# `Exercise 2` Name Counter

# 1. Generate a list with 100 elements, i.e ["johan", "lisa", "johan", "tove"...]
# 2. Count the names i.e ('lisa', 1), ('johan',2)
# 3. Print the top 3 most popular names
# 4. Print the least popular name[s]
# 5. Print all unique names
#    1. In alphabetical order
#    2. Shuffled
#    3. In reversed alphabetical order

# Start working on 6.2
from operator import indexOf
import random
from random import shuffle, choices, sample
from typing import Counter

separation = "==================================================="
seed_list = ["johan", "lisa", "tove", "tobias", "jonas", "sara"]
long_list = random.choices(seed_list, k = 100)

print(f"The list of all the names: {long_list}")
print(separation)

count_names = {}
for name in long_list:
    if name in count_names:
        count_names[name] += 1
    else:
        count_names[name] = 1
        
count = Counter(count_names)
common = count.most_common()


print(common)


print(f"The name count: {count_names}")
print(separation)
print(f"The most popular names: {count}")
print(separation)
print(f"The first 3 most polular names: {common[0:3]}")

print(separation)



print(f"Names in alphabetical order: {common.sort()}")
print(f"Names in shuffled order: {common}")
print(f"Names reverse alphabetical order: {common.reverse()}")



# use this
print([tup[0] for tup in common])