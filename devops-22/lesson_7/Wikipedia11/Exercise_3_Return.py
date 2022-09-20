# 1. Create a function that returns a integer
# 2. Create a function that returns a tuple with (x, y) value
# 3. Create a function that returns a boolean value
# 4. Create a function that returns a float
# 5. Create a function that has `firstname` and `lastname` as parameters and returns fullname.
# 6. Create a function that calculates the area of a rectangle and returns the result
# 7. Create a function that expects a list as argument, the list should contain integers and the function 
# 7.1 should return the sum of all elements in the list.
# 8. Create a function that repeats a word multiple time, `word` and `repeat` is used as parameters. 
# 8.1 If the word is hello and repeat is 3, it will print hello three times.

import random

# ------------------------------------EXERCISE 1------------------------------------

def intiger():
    return random.randint(0, 101)

# ------------------------------------EXERCISE 2------------------------------------

# No need for () here, if wrote with a "," it'll will always be
# returned as a tuple

def tuple(x, y):
    return (x, y)

# ------------------------------------EXERCISE 3------------------------------------

def boolean():
    return False

# ------------------------------------EXERCISE 4------------------------------------

def float():
    rand_float = random.random()
    return rand_float

# ------------------------------------EXERCISE 5------------------------------------

def name(firstname, lastname):
    return firstname + " " + lastname

# ------------------------------------EXERCISE 6------------------------------------

def area_rectangle(h, b):
    return h * b

# ------------------------------------EXERCISE 7------------------------------------


def sum_int_list(num_list=[]):
    return sum(num_list)

# ------------------------------------EXERCISE 8------------------------------------

def word_repeat(word, repeat):
    return word * int(repeat)
