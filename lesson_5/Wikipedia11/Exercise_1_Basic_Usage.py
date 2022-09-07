# 1. Print first, lastname and tele on the same line
# 2. Create a variable fullname
# 3. Assign to the new variable fullname, firstname and lastname separated with a space.
# 4. Print the length len() of fullname, firstname and lastname
# 5. Print a escape sequence \n so the first line contains fullname, and the second line tele.
# 6. Write the fullname and tele with the four different methods:
    # 6.1 Only using print() and string concatenation i.e "firstname" + " " ..
    # 6.2 Using f-string
    # 6.3 Using format, i.e print('{}'.format(firstname))
    # 6.4 Using printf (%) syntax, i.e print('A name %s' % firstname)

firstname = "Fredrik"
lastname = "Magnusson"
phone = "0046766331231"


# ------------------------------------EXERCISE 1------------------------------------

print(firstname, lastname, phone)

# ------------------------------------EXERCISE 2------------------------------------

fullname = ""

# ------------------------------------EXERCISE 3------------------------------------

fullname = firstname + " " + lastname
print(fullname)

# ------------------------------------EXERCISE 4------------------------------------

print(len(fullname))
print(len(firstname))
print(len(lastname))

# ------------------------------------EXERCISE 5------------------------------------

print(f"{fullname}\n{phone}")

# ------------------------------------EXERCISE 6------------------------------------

print(fullname + " " + phone)
print(f"{fullname} {phone}")
print("{}".format(fullname + " " + phone))
print("%s" % fullname, phone)