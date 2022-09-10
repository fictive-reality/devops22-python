########################################################################################################################
# Exercise 3 Unicode
# How to write a euro sign can be found at Currency Symbols. How to write emoji can be found at emoji, 
# you can also check the formal charts for symbols you use either name or code: \N{money-mouth face}, or code \U0001F911
# Write a program that fulfills the specification
# Let the user input a price, i.e Your new car cost: 1000000
# Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
# Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 
# use one emoji, if is above another one
########################################################################################################################

money_sign = "\U000020AC"
thinking_sign = "\U0001F914"
screaming_sign = "\U0001F631"
price = int(input("How much did you pay for your car? "))
print(f"Wow, did your car cost {price}{money_sign}?")
if price > 50000:
    print(f"{screaming_sign} Ouch, that was expensive.")
    
else:
    print(f"{thinking_sign} Hmmm, i like it, maybe i should get one myself.")
