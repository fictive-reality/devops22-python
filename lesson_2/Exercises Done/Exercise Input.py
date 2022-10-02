# # Exercise Input

# # Create a program that uses input and type conversion

# Input a string and assign it to a variable, then print the variable
# Input a number and assign it to a variable, print the value doubled
# Input a string i.e hello and assign it to a variable, print the string repeated hellohello
# Input a float and assign it to a variable, print the value divided by 3.5

password = input(f'Write your password here: ')
print(f'Your password is {type(password)}{password}')

doubled_value = input(f'Write a number and get it doubled: ')
print(f'You wrote number {doubled_value} and got it doubled to {int(doubled_value)*2}')

repeat_word = input(f'Write a word here: ')
print(f'I am repeating what you wrote {str(repeat_word)*10}')

float_number = input(f'Write a float number: ')
print(f'Your number {float(float_number)} divided by 3.5 result in: {float(float_number)/3.5}')