# Denna delen tar en annan input från användaren som måste bara en INT(Siffra)
# Problemet är att det tolkas som en string av python så jag måste konvertera den till
# en Integer
# Den blir utfört på rad 13
# Jag tänkte städa upp min kod lite och hittade att det går att ta int eller float direkt från input så att man inte behöver konvertera

number = int(input("Skriv ett nummer: "))
print(number * 2)

# print(type(int(number)))
# number_2 = int(number)
# print(type(int(number)))