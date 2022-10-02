# Slice

# Slice can be used to get a substring, i.e to get all but last letter my_string[:-1], to get all except the first letter my_string[1:], to get three first letters my_string[:3]

# Docs about slice

# Use slice to get the first 5 characters i fullname
# Use slice to get all characters except the first and last one
# Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
# Use slice to print a word backwards.
# Use slice to get the 5th character

tele = '0735986469'
fullname = "johan åsgard"
firstname = 'johan'
lastname = 'åsgard'
print(f'The first 5 characters i fullname: {fullname[:5]}')
print(f'{fullname[1:11]}')
print(f'{fullname.upper()[::2]}')
print(f'{fullname[::-1]}')
print(f'{fullname[5:6]}')

