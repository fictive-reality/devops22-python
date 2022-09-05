
# https://docs.python.org/3/library/stdtypes.html#list
# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

# Create a list with square brackets []
list_square = ["first", "second", "third"]
print(
    f'[1] list_square is of type {type(list_square)} with value: {list_square}')

# You can create a empty list with the built-in list()
list_builtin = list()
print(
    f'[2] list_builtin is of type {type(list_builtin)} with value: {list_builtin}')

# You can create a list of a iterable with the built-in list(iteratable)
list_builtin_iterable = list([1, 2, 3])
print(
    f'[3] list_builtin_iterable is of type {type(list_builtin_iterable)} with value: {list_builtin_iterable}')

# To access the first element use index 0
example_list = [10, 20, 30]
print(f'[4] index 0 is {example_list[0]}')

# To access the last tuple slot use index len() - 1
example_list = [10, 20, 30]
last_index = len(example_list) - 1
print(f'[5] last_index is {last_index}')
print(f'[6] example_list[last_index] is {example_list[last_index]}')
print(f'[7] example_list[2] is {example_list[2]}')


# You can assign new value to a list
my_list = ["1", "7", "3"]
my_list[1] = "2"
print(f'[8] my_list is {my_list}')

# You can append new elements to the list
print(f'[9] my_list is of len {len(my_list)} and with elements {my_list}')
a_value = "4"
my_list.append(a_value)
my_list.append("5")

print(
    f'[10] after appending two times my_list is of len {len(my_list)} and with elements {my_list}')

# Remove the first element

del my_list[0]
print(
    f'[11] after del my_list[0], my_list is of len {len(my_list)} and with elements {my_list}')

# Pop the last element if no index is provided
my_list.pop()
print(
    f'[12] after my_list.pop(), my_list is of len {len(my_list)} and with elements {my_list}')

# You can remove elements without knowing their index
my_list.remove('3')
print(
    f'[13] after my_list.remove("3") it is of len {len(my_list)} and with elements {my_list}')
