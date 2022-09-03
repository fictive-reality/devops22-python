# Exercise 2 Printing

# Print a integer value
a = 1
print(f"a it's a variable of type {type(a)} and with a value of {a}")

# Print a float value
b = 1.5
print(f"b it's a variable of type {type(b)} and with a value of {b}")

# Print a String
c = "this is a string"
print(f"c it's a variable of type {type(c)} and with a value of {c}")

# Print a boolean value
d = False
print(f"d it's a variable of type {type(d)} and with a value of {d}")

# Print a None value
e = None
print(f"e it's a variable of type {type(e)} and with a value of {e}")

# Print a f-string containing all previous values in one line i.e 1, 1.0, "hello" ..
print(f"{a, b, c, d, e}")

# Exercise 2 Input

# Input a string and assign it to a variable, then print the variable
username = input("Who are you? ")
print("Your name is " + username)
print(f"Hi there {username}")

# Input a number and assign it to a variable, print the value doubled
number = input("Input a number: ")
double = int(number) * 2
print(double)

# Input a string i.e hello and assign it to a variable, print the string repeated hellohello
greatings = input("Input a greating: ")
print(greatings + greatings)

# Input a float and assign it to a variable, print the value divided by 3.5
floaty = input("Input a real number: ")
divide = float(floaty) / float(3.5)
print(f"{floaty} divided by 3.5 equals = {divide}")