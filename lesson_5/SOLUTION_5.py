firstname = "john"
lastname = "smith"
tele = "00468123456789"
### `Exercise 1` Basic usage
# 1. Print first, lastname and tele on the same line

print(f"{firstname} {lastname} {tele}")

# 2. Create a variable fullname
# 3. Assign to the new variable fullname, firstname and lastname separated with a space.
fullname = f"{firstname} {lastname}"

# 4. Print the length `len()` of fullname, firstname and lastname
print (len(fullname), len(firstname), len(lastname))
# 5. Print a escape sequence `\n` so the first line contains fullname, and the second line tele.

print ( f"{fullname}\n{tele}")

# 6. Write the fullname and tele with the four different methods:
#    1. Only using print() and string concatenation i.e "firstname" + " " ..
print(firstname + " " + lastname)
#    2. Using f-string
print(f"{firstname} {lastname}")

#    3. Using format, i.e print('{}'.format(firstname))

print("{first} {last}".format(first=firstname, last=lastname))

#    4. Using printf (%) syntax, i.e print('A name %s' % firstname)

print("%s %s" % (firstname, lastname))

### `Exercise 2` Slice

# 1. Use slice to get the first 5 characters i fullname
print(fullname[0:5])
# 2. Use slice to get all characters except the first and last one
print(fullname[1:-1])
# 3. Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
print(fullname[::2].upper())

# 4. Use slice to print a word backwards.
print(fullname[::-1])
# 5. Use slice to get the 5th character
print(fullname[4:5])

### `Exercise 3` Unicode

# Write a program that fulfills the specification

# 1. Let the user input a price, i.e Your new car cost: 1000000
# 2. Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
# 3. Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 use one emoji, if is above another one

price = int(input("Your new car costs? "))
print(f"Your new car costs: {price}\u20BF")
if price < 50000:
    print("\N{grinning face}")
else:
    print("\U0001F606")
