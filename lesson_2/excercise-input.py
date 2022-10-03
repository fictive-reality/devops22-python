#  `Exercise` Input

# Create a program that uses input and type conversion


# 1. Input a string and assign it to a variable, then print the variable
my_name = input("What is your name?: ")
print(my_name)

# 2. Input a number and assign it to a variable, print the value doubled
your_age = input("How old?: ")
print(f"Your age is {int(your_age)*2}")

# 3. Input a string i.e `hello` and assign it to a variable, print the string repeated `hellohello`
my_text = input("What you write will be doubled: ")
print(f"{(my_text)*2}")

# 4. Input a float and assign it to a variable, print the value divided by 3.5
money_left = float(input("Money left?: "))
money_left /= 3.5
print(f"Your money left is {(money_left)} SEK")
