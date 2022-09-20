# Generate a list of lowercase a-z
# Iterate through the alphabet and append each letter to a stack
# Pop all elements and print on one line as a string

from inspect import stack
import string

# ------------------------------------EXERCISE 1------------------------------------

lower_case = list(string.ascii_lowercase)
print(lower_case)
# ------------------------------------EXERCISE 2------------------------------------

stack_alpha = []

for l in lower_case:
    stack_alpha.append(l)
print(stack_alpha)

print(type(stack_alpha))

# ------------------------------------EXERCISE 3------------------------------------

alphabet_str = ""
for i in range(len(stack_alpha)):
    alphabet_str =  alphabet_str + stack_alpha.pop() + " "

print(alphabet_str)