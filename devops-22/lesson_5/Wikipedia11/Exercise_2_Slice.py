# Slice can be used to get a substring, i.e to get all but last letter my_string[:-1], 
# to get all except the first letter my_string[1:], 
# to get three first letters my_string[:3]

# Docs about slice # https://docs.python.org/3/library/functions.html#slice

# 1. Use slice to get the first 5 characters i fullname
# 2. Use slice to get all characters except the first and last one
# 3. Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
# 4. Use slice to print a word backwards.
# 5. Use slice to get the 5th character


firstname = "Fredrik"
lastname = "Magnusson"
phone = "0046766331231"
fullname = firstname + " " + lastname

# ------------------------------------EXERCISE 1------------------------------------

print(fullname[0:5])

# ------------------------------------EXERCISE 2------------------------------------
num_of_char = len(fullname) - 1
print(fullname[1:num_of_char])

# ------------------------------------EXERCISE 3------------------------------------
num_of_char = len(fullname)
print(fullname[::2])

# ------------------------------------EXERCISE 4------------------------------------

print(fullname[::-1])

# ------------------------------------EXERCISE 5------------------------------------

print(fullname[4])



