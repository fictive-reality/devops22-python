from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(x=7, y=5)

# Print Point
print(p)

# Get x from point
print(p[0])  # Use index
print(p.x)  # Use field

# Namedtuple example
Fullname = namedtuple('Fullname', ['first', 'last'])

name = ["Olle", "Svensson"]
f = Fullname._make(name)
print(f)

# Print fields
print(f._fields)
