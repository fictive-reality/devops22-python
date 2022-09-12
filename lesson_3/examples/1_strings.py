# https://docs.python.org/3/library/stdtypes.html#string-methods

a_string = "hellO wOrld"

# You can ask if a string is lower or is upper
print(f'[1] a_string.islower() {a_string.islower()}')

# You can make the first letter capitalized
print(f'[2] a_string.capitalize() {a_string.capitalize()}')

# You can make every words first letter uppercase
print(f'[3] a_string.title() {a_string.title()}')

# You can write the whole string as upper
print(f'[4] a_string.upper() {a_string.upper()}')

# String is immutable, the method will produce a new string, so this is still false
print(f'[5] a_string.isupper() {a_string.isupper()}')

# You can reassign the string, then it's True
a_string = a_string.upper()
print(f'[6] a_string.isupper() {a_string.isupper()}')
