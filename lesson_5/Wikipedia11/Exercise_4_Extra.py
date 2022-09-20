# Write a program that handles salary negotiations. The user is the employee and the boss is your program.

# 1. The boss tells the user it's current salary and currency
# 2. The employee ask for more money with an input. I.e 2000 more
# 3. The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
# 4. The employee ask again for another amount i.e 1800
# 5. The boss calculates the percentage and respond yes or no, you decide which criteria the boss uses. 4 and 5 iterates in a loop until the employee quit or the boss accept the amount.

# ------------------------------------EXERCISE 4------------------------------------

current_sallery = 2500

print(f"You current sallery is €{current_sallery}")
emp_raise = int(input("How much of a raise are you looking for? €"))

# emp_raise / current_sallery * 100 = raise in percent

percent_raise = emp_raise / current_sallery * 100 
emp_raise = int(input("\U0001f645" " Please counter give a lower suggestion: "))
while True:
    if percent_raise > 3:
        emp_raise = int(input("\U0001f645" " Please counter give a lower suggestion: "))
        percent_raise = emp_raise / current_sallery * 100 
    else:
        new_sallery = current_sallery + emp_raise
        print(f"Congratulations, your new salery will be €{new_sallery}")
        break