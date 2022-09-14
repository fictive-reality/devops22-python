
# Create testdata
one_to_ten = list(range(1, 11))
print(one_to_ten)

# Print all values
print(sum(one_to_ten))

# Use a lambda to filter values
# Keep value if its 2
only_keep_twos = filter(lambda x: x == 2, one_to_ten)
print(list(only_keep_twos))

# Use a lambda to filter values
# keep values above 4
above_four = filter(lambda x: x > 4, one_to_ten)
print(list(above_four))

# Sum all odd values in a list?
# sum(1, 3, 5, 7, 9) = 25
print(sum(filter(lambda x: x % 2, one_to_ten)))
