# 1. Create a function that prints 1 to 10 by default, i.e `start=1` `stop=11` and uses a range in the function block.
# 2. Create a function that by default prints a string, if `reverse=True` is used as argument the 
# 2.1string is printed in reverse.
# 3. Call the same function with and without reverse

# ------------------------------------EXERCISE 1------------------------------------

def number(start=1, stop=11):
    for n in range(start, stop):
        print(n)

# ------------------------------------EXERCISE 2 & 3------------------------------------

def string_reverse(word, reverse=True):
    if reverse:
        print(word[::-1])
    else:
        print(word)