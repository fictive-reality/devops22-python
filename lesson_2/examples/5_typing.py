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
