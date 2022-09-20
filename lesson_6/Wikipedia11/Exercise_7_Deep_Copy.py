# Create a list with names
# Assign the list to a variable
# Create a copy and a deep copy
# pop one element in the original list and append a new name
# Print all lists, what differs?

from copy import copy
from copy import deepcopy
from unicodedata import name

# ------------------------------------EXERCISE 1------------------------------------

name_list = ["Fredrik", "Johanna", "Mari", "Lars", "Carolina", "Pontus"]

# ------------------------------------EXERCISE 2------------------------------------

var_1 = name_list

# ------------------------------------EXERCISE 3------------------------------------

var_2 = copy(name_list)
var_3 = deepcopy(name_list)

# ------------------------------------EXERCISE 4------------------------------------

name_list.pop()
name_list.append("Tuva")

# ------------------------------------EXERCISE 5------------------------------------

print(var_1)
print(var_2)
print(var_3)