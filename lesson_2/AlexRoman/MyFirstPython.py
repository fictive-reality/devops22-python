# Output
# Print a string
print("hello world")

# Print a expression
print(1+2)

# f-string
print(f"1+2 is { 1+2 }")

# Binary Operations
# https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations

# + addition
print(1 + 1)

# - substraction
print(1 - 1)

# * multiplication
print(5*2)

# / division
print(5/2)

# // floor division
print(5//2)

# % modulo
print(5 % 2)

# Assignment
# You can bind a variable name to a value with a Assignment Statement
# https://docs.python.org/3/reference/simple_stmts.html#assignment-statements

# a_variable is the name
# 5 is the value
a_variable = 5

# https://docs.python.org/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations
# You can use the unary operation - to create a negative integer
negative_value = -1

# You can rebind a variable
a_variable = "hello world"
a_variable = 5

# You can bind another_variable
another_variable = 5 + 2

# a_variable + another_variable is a expression and it will be evaluated before assignment
the_third_variable = a_variable + another_variable

# You can assign multiple variable in one line
x = y = z = 2

# Augmented assignment
# https://docs.python.org/3/reference/simple_stmts.html#augmented-assignment-statements

result = 1

# addition and assignment
result += 2
print(f'[1] {result}')

# subtraction and assignment
result -= 1
print(f'[2] {result}')

# multiplication and assignment
result *= 10
print(f'[3] {result}')

# modulus and assignment
result %= 8
print(f'[4] {result}')

# division and assignment
result /= 2
print(f'[5] {result}')

# pow and assignment
result **= 3
print(f'[6] {result}')

# floor division and assignment
result //= 2
print(f'[7] {result}')

# Typing 
# BASIC TYPES

# integer
a = 1
print(f'a is of type {type(a)} and with a value of {a}')

# float
b = 1.0
print(f'b of type {type(b)} and with a value of {b}')

# string
c = "hello world"
print(f'c of type {type(c)} and with a value of {c}')

# boolean
d = True
print(f'd of type {type(d)} and with a value of {d}')

# None
e = None
print(f'e of type {type(e)} and with a value of {e}')

# Change type

price = "100"
print(f'price is of type {type(price)} and with a value of {price}')

# This will not work as expected, what happens?
price *= 2
print(f'price is of type {type(price)} and with a value of {price}')

# This will work as expected, what's the difference?
price = "100"
price = int(price) * 2
print(f'price is of type {type(price)} and with a value of {price}')

# Input
# Get input from user
my_name = input("Write your name: ")
print(f"hello {my_name}")

# input is of type
print(f"my_name is of type {type(my_name)}")

# If you want a integer you must convert the type with int()
my_age = input("Please enter your age: ")
print(f"Next year I will be {int(my_age) + 1} years old")
