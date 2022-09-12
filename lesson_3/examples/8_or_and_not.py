# https://docs.python.org/3/reference/expressions.html#boolean-operations


# https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not​
x = False
y = True

# Or
result = x or y
print(f'[1] x or y results in: {result}')

# And
result = x and y
print(f'[2] x and y results in: {result}')

# Not
print(f'[3] x is {x},  not x results in: {not x}')
print(f'[4] y is {y}, not y results in: {not y}')

# Not in combination with and
result = not x and y
print(f'[5] not x and y results in: {result}')
