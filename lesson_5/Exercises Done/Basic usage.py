# Basic usage

# Print first, lastname and tele on the same line
# Create a variable fullname
# Assign to the new variable fullname, firstname and lastname separated with a space.
# Print the length len() of fullname, firstname and lastname
# Print a escape sequence \n so the first line contains fullname, and the second line tele.
# Write the fullname and tele with the four different methods:
# Only using print() and string concatenation i.e "firstname" + " " ..
# Using f-string
# Using format, i.e print('{}'.format(firstname))
# Using printf (%) syntax, i.e print('A name %s' % firstname)


print('johan åsgard 0735986469')
tele = '0735986469'
fullname = "johan åsgard"
firstname = 'johan'
lastname = 'åsgard'
print(f'Length of fullname, firstname and lastname: {len(fullname),len(firstname),len(lastname)}')
print(f'{fullname}\n{tele}')
print('johan'' '+'åsgard'' '+'0735986469')
print(f'{fullname.title()}, {fullname.swapcase()}, {fullname.splitlines()}, {fullname.lower()},{fullname.upper()}, {fullname.rstrip()}, {fullname.format()}')

#using .format()
print(f'{firstname} {lastname} {tele}'.format(
firstname = 'johan',
lastname = 'åsgard',
tele = '0735986469'))

#using printf (%) syntax
print('Fistname: %s,' % firstname.title())
print('Lastname: %s,' % lastname.title())
# %s - fot str and if you changed it to %d its only for int 
print(f'Tele: %d,' % int(tele))

