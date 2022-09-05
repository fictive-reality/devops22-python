##########################################################
#  Exercise 1 even or odd                                #
#  Write a program that fulfills the specification:      #
#    1. Ask the user for a integer                       #
#    2. If the integer is even, print even               #
#    3. If the integer is odd, print odd                 #
##########################################################

user_number = int(input("Enter a integer: "))

if(user_number % 2 == 0):
    print(f"Your number {user_number} is even")
else:
    print(f"Your number {user_number} is odd")
