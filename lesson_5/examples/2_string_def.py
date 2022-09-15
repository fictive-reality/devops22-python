
"""
A string is a sequence of values that represent Unicode code points.
All the code points in the range U+0000 - U+10FFFF can be represented in a string.
Python doesn’t have a char type; instead,
every code point in the string is represented as a string object with length 1.
The built-in function ord() converts a code point from its string form to an integer in the range 0 - 10FFFF;
chr() converts an integer in the range 0 - 10FFFF to the corresponding length 1 string object.
str.encode() can be used to convert a str to bytes using the given text encoding,
and bytes.decode() can be used to achieve the opposite.
"""

# Null is not printable
print("a\u0000b")

# Ord of letter a
ord_a = ord('a')
print(ord_a)
# Print as hex
print(f'0x{ord_a:04x}')
print(chr(97))

# Unicode a
print('\u0061')


my_string = "hello world"
print(f'my_string: [{my_string}] is of type {type(my_string)}')
print(f'my_string[0]: [{my_string[0]}] is of type {type(my_string[0])}')


# Encode & decode

my_string = "hello world"
my_bytes = my_string.encode()
print(f'Type of my_bytes is {type(my_bytes)}')
print(my_bytes)

decoded = my_bytes.decode()
print(f'my_bytes decoded: [{decoded}] type is {type(decoded)}')
