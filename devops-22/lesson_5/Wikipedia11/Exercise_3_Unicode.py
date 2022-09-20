

# How to write a euro sign can be found at Currency Symbols(https://www.unicode.org/charts/PDF/U20A0.pdf). How to write emoji can be found at emoji, 
# you can also check the formal charts for symbols(https://www.unicode.org/charts/#symbols) you use either name or code: \N{money-mouth face}, or code \U0001F911

# Write a program that fulfills the specification

# 1. Let the user input a price, i.e Your new car cost: 1000000
# 2. Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
# 3. Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 use one emoji, if is above another one

# ------------------------------------EXERCISE 1 & 2------------------------------------

price_of_car = int(input("Your new car costs: \N{euro sign}"))

# ------------------------------------EXERCISE 3------------------------------------

if price_of_car <= 1000:
    print(u"\U0001F4A9")
elif price_of_car <= 10000:
    print(u"\U0001F92E")
elif price_of_car <= 100000:
    print(u"\U0001F648")
else:
    print(u"\N{money-mouth face}")