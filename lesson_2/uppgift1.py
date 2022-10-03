#Execrise 1

# bound variable to an integer value, and print result.

num = 3
print(num)

my_num = 5
print(str(my_num))


# bound variable to float value

inf  = 3.5
print(inf)

# string
my_name = "Emmanuel"
print(my_name)

print("Emmanuel Frank")
print("Emmanuel\nFrank")

# boolean value

X = 200
Y = 100

if Y > X :
 print("X is greater than Y")
else:
 print("X is not greater than Y")

# print none valve

X = None
print(X)


# Print a f-string containing all previous values 

print(f' {num}, {my_num}, {inf}, {my_name}, {X}')


### `Exercise` Input

#Input a string and assign it to a variable, then print the variable

username = input("Enter username:")
print("username is" + username)

name = input("Enter name")
print(f'Your name is {name}') 

# Input a number and assign it to a variable, print the value doubled

int_valve = input("Please enter your age:")
print(f'your age is:{int(int_valve) *2}')

int_value =int(input("write integer value:"))
print(int_value *2)

int_value =int(input("write integer value:"))
print(f'your number is {int(int_value) *2}')

text = input("text:")
print(text *20)

#Input a float and assign it to a variable, print the value divided by 3.5

num = float(input("Write a flaot number:"))
print(num / 3.5)