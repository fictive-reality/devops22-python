
# https://docs.python.org/3/library/stdtypes.html#tuples

# You should create a tuple by using paranthesis ()
from typing import MutableMapping


tuple_paranthesis = (5, 3, 4)
print(
    f'[1] tuple_paranthesis is of type {type(tuple_paranthesis)} with value: {tuple_paranthesis}')

# You can create a tuple with a comma ,
tuple_comma = 5, 3, 4
print(
    f'[2] tuple_comma is of type {type(tuple_comma)} with value: {tuple_comma}')

# You can create a tuple with the built-in tuple(iterable)
tuple_builtin = tuple([1, 2, 3])
print(
    f'[3] tuple_builtin is of type {type(tuple_builtin)} with value: {tuple_builtin}')

# To access the first element use index 0
example_tuple = (10, 20, 30)
print(f'[4] index 0 is {example_tuple[0]}')

# To access the last tuple slot use index len() - 1
example_tuple = (10, 20, 30)
last_index = len(example_tuple) - 1
print(f'[5] last_index is {last_index}')
print(f'[6] example_tuple[last_index] is {example_tuple[last_index]}')
print(f'[7] example_tuple[2] is {example_tuple[2]}')


# You can't assign new item to a tuple
my_tuple = ("hello", "world")
# TypeError: 'tuple' object does not support item assignment
