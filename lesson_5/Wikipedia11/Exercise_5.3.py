# Följande strängmetoder får användas:
# (a) capitalize()  Converts the first character to upper case
# (b) join()        Joins the elements of an iterable to the end of the string
# (c) lower()       Converts a string into lower case
# (d) upper()       Converts a string into upper case
# (e) swapcase()    Swaps cases, lower case becomes upper case and vice versa
# (f) replace()     Returns a string where a specified value is replaced with a specified value
# (g) split()       Splits the string at the specified separator, and returns a list
# (h) rsplit()      Splits the string at the specified separator, and returns a list
# (i) title()       Converts the first character of each word to upper case
# (j) format()      Formats specified values in a string

mening_str = "Jag tYcker om äGg"
inte_str = "inte"
spam_str = "SPAM"
mellanslag_str = " "

print(f"Jag börjar med en string som ser ut så här: \"{mening_str}\"\n")

mening_str = mening_str.lower()
print(f"Där efter gör jag om alla bokstäver till små med lower(): \"{mening_str}\"\n")

ord = mening_str.split()
print(f"Nu kommer jag att splitta upp alla ord och lägga in dom i en lista: \"{ord}\"\n")

ord.insert(2, inte_str)
print(f"Lägger till ordet \"inte\" i listan med index 2: \"{ord}\"\n")

mening_str = mellanslag_str.join(ord)
print(f"Gör tillbaka allt till en string med .join() där jag använder mig av mellanslag stringen: \"{mening_str}\"\n")

mening_str = mening_str.title()
print(f"Nu måste jag göra första karaktären i varje ord stor bokstav med .title(): \"{mening_str}\"\n")

mening_str = mening_str.swapcase()
print(f"Nu behöver jag ändra så att alla små bokstäver blir stora och tvärtom, det gör jag med .swapcase(): \"{mening_str}\"\n")

mening_str = mening_str.replace("ägg", inte_str)
print(f"Sist men inte minst så byter jag ut ordet \"äGG\" mot \"SPAM\" med .replace(): \"{mening_str}\"\n")

print(f"Slutgiltligt resultat är: \"{mening_str}\"")



