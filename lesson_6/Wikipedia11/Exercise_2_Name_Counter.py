# Generate a list with 100 elements, i.e ["johan", "lisa", "johan", "tove"...]
# Count the names i.e ('lisa', 1), ('johan',2)
# Print the top 3 most popular names
# Print the least popular name[s]
# Print all unique names
# In alphabetical order
# Shuffled
# In reversed alphabetical order

from collections import Counter
import random

# ------------------------------------EXERCISE 1------------------------------------

names = ["Fredrik", "Johanna", "Mari", "Lars", "Carolina", "Pontus", "Tuva", "Siri"]
name_list = random.choices(names, k=100)

# ------------------------------------EXERCISE 2------------------------------------

c = Counter(name_list)

# ------------------------------------EXERCISE 3------------------------------------

print('Top 3 common names')
print(c.most_common(3))

# ------------------------------------EXERCISE 4------------------------------------

print("Least common name")
print(c.most_common()[-1])

# ------------------------------------EXERCISE 5------------------------------------

unique = list(set(names))
print(unique)

# ------------------------------------EXERCISE 5.1------------------------------------

print(sorted(names))

# ------------------------------------EXERCISE 5.2------------------------------------

random.shuffle(unique)
print(unique)

# ------------------------------------EXERCISE 5.3------------------------------------

print(sorted(unique, reverse=True))