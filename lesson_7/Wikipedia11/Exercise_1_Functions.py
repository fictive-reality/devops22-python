# 1. Create a function with name `do_nothing`
#    1. The function should have a `pass`
#    2. Call the function from your code
# 2. Functions getting started:
#    1. Create a function that prints `hello world`
#    2. Create a function that prints the result from `1 == 1.0`
#    3. Create a function that prints the alphabet in reverse order
# 3. Functions with arguments
#    1. Create a function that prints `hello name` with name as a parameter
#    2. Create a function that prints a string in capital letters, with `word` as a parameter
#    3. Create a function that prints numbers between 1 and `stop`, where stop is a parameter

import string
# ------------------------------------EXERCISE 1------------------------------------

def do_nothing():
    pass

# ------------------------------------EXERCISE 2------------------------------------

def hello_world():
    print("hello world")

def numbers():
    print(1 == 1.0)

def alphabet():
    print(string.ascii_lowercase[::-1])
# ------------------------------------EXERCISE 3------------------------------------

def hello_name(name):
    print("Hello, " + name + ". Good morning!")

def upper_string(word):
    print(f"{word.upper()} ")

def num_print(stop, start=1):
    for n in range(start, stop):
        print(n)

