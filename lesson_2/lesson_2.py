from operator import truediv
from pickle import NONE
###PRINTING###

a = 22
print(a) # Integer

b = 22.22
print(b) #Float

c = "hello world"
print(c) #string

x = 10
y = 11
print(x == x) #boolean
print(x == y) #boolean

f = NONE #None
print(f)

print (f'{a}, {b}, {c}, {x==x}, {x==y}, {f}') #f-string


###INPUT###

name = input ("Write your name: ") #1
print(f"Your name is: {name}")

age = input ("Write your age: ") #2
print(f"Double your age is: {int(age) * 2}")

phrase = input ("Write something: ") #3
print(phrase,phrase)

number = input ("Write a float value: ") #4
print(f"{int(number) / 3.5} ")