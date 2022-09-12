# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

my_cars = {"abc123": ("volvo", "xc60")}

# To access a value, use the key
print(f'[1] my_cars["abc123"] {my_cars["abc123"]}')

# To add a value you can
my_cars["abc456"] = ("saab", "900")

# To print all keys and values
print(f'[2] my_cars {my_cars}')

# To print all keys
print(f'[3] list(my_cars) {list(my_cars)}')

# To print all values
print(f'[4] list(my_cars.values()) {list(my_cars.values())}')

# You can also use a method to add multiple values
my_cars.update({"abc678": ("kia", "niro"), "abc910": ("toyota", "rav4")})
print(f'[5] my_cars {my_cars}')


# If you first print a dict value
print(f'[6] my_cars["abc678"] {my_cars["abc678"]}')

# Then you delete it by key and try to print again, it will fail
del my_cars['abc678']
# print(f'[7] my_cars["abc678"] {my_cars["abc678"]}')
