# Create variable with a string
# Create second variable and assign the first variable to it
# Create a third variable and assign a copy of the first variable
# Change the second variable
# Print all variables, what differs?

# ------------------------------------EXERCISE 1------------------------------------

from copy import copy


var_1 = "Hej, Jag heter"

# ------------------------------------EXERCISE 2------------------------------------

var_2 = var_1

# ------------------------------------EXERCISE 3------------------------------------

var_3 = copy(var_1)

# ------------------------------------EXERCISE 4------------------------------------

var_2 += " Fredrik"

# ------------------------------------EXERCISE 5------------------------------------

print(var_1)
print(var_2)
print(var_3)