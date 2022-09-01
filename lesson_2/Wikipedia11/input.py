# Denna delen tar input från användaren och printar tillbaka den inputen i terminalen

username = input("Enter username: ")
print("username is: " + username)

# Denna delene tar en annan input från användaren som måste bara en INT(Siffra) '
# Problemet är att det tolkas som en string av python så jag måste konvertera den till
# en Integer
# Den blir utfört på rad 13

number = input("Skriv ett nummer: ")
# print(type(int(number)))
number_2 = int(number)
print(number_2 * 2)
# print(type(int(number)))

# Denna delen tar input från användaren och dubblar ordet som användaren har gett koden

Double_string = input("Skriv en ny string: ")
print(Double_string * 2)

# Denna delen tar input frår användaren, i ett float nummer (Nummer med decimal) 
# och dividerar den numret med 3.5
# Igen så måste jag göra en konversation från str (string) till float, skrev på rad 27

float_input = input("Skriv ett nummer med minst en decimal: ")
float_float = float(float_input)
print(float_float / 3.5)


# number = 20 * 3
# print("The product is: ", number)