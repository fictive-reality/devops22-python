##############################################################################################################################
# Exercise 4 Extra
# Write a program that handles salary negotiations. The user is the employee and the boss is your program.
# The boss tells the user it's current salary and currency
# The employee ask for more money with an input. I.e 2000 more
# The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
# The employee ask again for another amount i.e 1800
# The boss calculates the percentage and respond yes or no, you decide which criteria the boss uses. 4 and 5 iterates 
# in a loop until the employee quit or the boss accept the amount.
##############################################################################################################################


salary = int(input("Please input your salary "))
print(" Ok, so whe got to that time of the year when we have to see if you get a raise")
print(f"Today you have a salary of {salary}")
first = int(input("How much raise are you expecting?"))
second = int(input("Unfortunatelly i have to refuse your proposal, other numbers in mind?"))
another_try = 1
percentage = int((second/(salary/100)))
print(percentage) 
if percentage < 3:
    print(f"{another_try} sound's about right! We have a deal")
else:
    print(f"{another_try} it's a bit too much. How low can you go?")

