# Minimal class

class A:
    pass

# Instantiating a Class
# Create a object


a = A()
print(a)  # <__main__.A object at 0x101adcd90>
print(type(a))  # <class '__main__.A'>

# Set a instance variable

a.color = 'red'
print(a.color)

# Try to use the instace variable in another instance
a_2 = A()
# print(a_2.color)

# Now try to set a class variable
A.color = 'blue'
a_3 = A()
a_3.color = "grey"
a_4 = A()

print(a_3.color)
print(a_4.color)

# Notice that Class variables will be the same for all instances

A.color = 'black'

print(a_3.color)
print(a_4.color)

# The instance variable is not changed
print(a.color)
