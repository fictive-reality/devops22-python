# Boolean Operations - and, or, not

# Create a program that creates three variables x, y, z as booleans. You can modify these variables to test your expressions.

# x = True
# y = False
# z = True
# Write a expression with Boolean Operations that:
# result in True if any of x, y, z is True
# result in True if all x, y, z is True
# result in False if any of x, y, z is False
# result in False if all of x, y, z is False
# result in False if any of z, y, z is True
# result in False if all of z, y, z is True

x = True
y = False
z = True

result = x or y or z
print(f'If any of x,y,z is True result is: {result}') 

x = True
y = True
z = True
result = x and y and z
print(f'If all of x,y,z is True result is: {result}') 

x = True
y = True
z = False
result =  x and y and z
print(f'If any of x,y,z is False result is: {result}') 

x = False
y = False
z = False

result =  x and y and z
print(f'If all of x,y,z is False result is: {result}') 

x = True
y = False
z = False

result =  not x and y and z
print(f'If any of x,y,z is True result is: {result}') 

x = True
y = True
z = True

result = not x and not y and not z
print(f'If all of x,y,z is True result is: {result}') 