#####################################################################################################
#  Exercise 2 VIP                                                                                   #
#  Write a program that fulfills the specification:                                                 #
#    1. Ask the user for a name                                                                     #
#    2. Create a tuple with at least five names                                                     #
#    3. If the user input is in the tuple, print the text "Welcome {name} your are on the list".    #
#    4. If the user input is not in the tuple, print "Sorry, you are not on the list".              #
#####################################################################################################


user_name = input("Enter your name: ").capitalize()
vip_list = ("Adam", "Eve", "John", "Michael", "Anders")

if(user_name in vip_list):
    print(f"Welcome {user_name}, you are on the list!")
else:
    print(f"Sorry, you are not on the list!")