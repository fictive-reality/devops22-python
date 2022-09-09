#Test
#Unicode
print('\U0001F600')
print('\N{GRINNING FACE}')
print('rad-1\u0085rad-2')

#Strängmetoder
namn='johaN anderssoN'
print(namn)
print(namn.title())
print(namn.swapcase())

#Slice
my_string="Hello World"

print(my_string[:1])
print(my_string[:5])
print(my_string[::2])
print(my_string[::-1])

# Python program to
# format a output using
# string() method

cstr = " I love Pyhton "

# Printing the center aligned
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))

# Printing the left aligned
# string with "-" padding
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))

# Printing the right aligned string
# with "-" padding
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))


# Python program showing how to use
# string modulo operator(%) to print
# fancier output

# print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % (25))

# print exponential value
print("%10.3E" % (356.08977))

print('\N{money-mouth face}')
print('\N{grimacing face}')
print('\N{face with tears of joy}')



