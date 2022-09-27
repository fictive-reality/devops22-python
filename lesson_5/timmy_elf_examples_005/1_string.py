### Format precision ###

# Create a float
number = 1/3
print(f"Number: {number}")

# Print float with two decimals
print(f"Number: {number:.2f}")

# Float
width = 4
precision = 4
value = 12.34567
print(f'float no formatting: {value}')
print(f'float width: {value:.{precision}}')
print(f'float precision: {value:.{precision}}')
print(f'float both: {value:{width}.{precision}}')

# Fill with *
credit_card = "5105105105105100"
print(f'{credit_card[:4]:*<12.6s}{credit_card[-4:]}')

### Format methods ###

# Format
firstname = 'john'
print('Good morning {}'.format(firstname))

# Old style % operator
print('Good morning %s' % firstname)

# f-strings
print(f'Good morning {firstname}')

# Concatenation
print("Good morning " + firstname)

### Slice ###
# Slicing strings
print(firstname[:3])

### Unicode ###
print('\N{money-mouth face}')
print('\U0001F911')

# Dollar
print('\u0024')