from secrets import choice
import string
from operator import itemgetter, mul
from random import shuffle, choices, sample
from typing import Counter

# Name Counter

# 1.
names = choices(["Adam", "Bertil", "Caesar", "David", "Erik","Filip", "Gustav", "Helge", "Ivar", "Johan"], k=100)

# 2.
counted_names = Counter(names)
print(counted_names)

# 3.
print(counted_names.most_common(3))

# 4.
print(counted_names.most_common()[-1])

# 5.
# i.
unique_names = sorted(list(set(names)))
print(unique_names)
# ii.
shuffle(unique_names)
print(unique_names)
# iii.
unique_names.sort(reverse=True)
print(unique_names)