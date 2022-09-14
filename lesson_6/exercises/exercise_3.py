import string


# Stack

# 1.
list(string.ascii_lowercase)

# 2.
this_stack = []
for character in string.ascii_lowercase:
    this_stack.append(character)

# 3.
this_string = ""
while this_stack:
    this_string += this_stack.pop()

print(this_string)