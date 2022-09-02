# https://docs.python.org/3/reference/expressions.html#comparisons
# https://docs.python.org/3/library/stdtypes.html#comparisons


my_list = [1, 4, 6]

# You can check if value exist in list
print(f'[1] 1 in my_list {1 in my_list}')
print(f'[2] 3 in my_list {3 in my_list}')

# You can negate with not
print(f'[3] 2 not in my_list {2 not in my_list}')


# You can use operator to compare values

low_value = 1
high_value = 10

# <
print(f'[4] low_value < high_value {low_value < high_value}')

# >
print(f'[5] low_value > high_value {low_value > high_value}')

# ==
print(f'[6] low_value == high_value {low_value == high_value}')

# >=
print(f'[7] low_value >= high_value {low_value >= high_value}')

# <=
print(f'[8] low_value <= high_value {low_value <= high_value}')

# !=
print(f'[8] low_value != high_value {low_value != high_value}')
