# 1. Import `sqrt` from `math`, calculate the sqrt of 16
# 2. Import `randint` from `random`, generate a random int 1 - 10
# 3. Import & Create a custom module
#    1. Create a module named `calc.py`
#    2. Add a function add that takes arguments x, y and return x + y.
#    3. Import and use the function from `calc.py`

from math import sqrt
from random import randint
from calc import addition
# ------------------------------------EXERCISE 1------------------------------------

print(sqrt(16))

# ------------------------------------EXERCISE 2------------------------------------

randomint = randint(1, 10)
print(randomint)

# ------------------------------------EXERCISE 3------------------------------------

print(addition(2, 2))

print(sqrt(addition(2, 6)))

# ------------------------------------EXERCISE 3.1------------------------------------



# ------------------------------------EXERCISE 3.2------------------------------------



# ------------------------------------EXERCISE 3.3------------------------------------