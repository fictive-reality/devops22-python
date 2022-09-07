from enum import unique


X = 1
Y = 4

addresses = {"Adam": "Ormvägen 5","Bella": "Klockgatan 1","Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

addresses["Daniel"] = "Prinsgränd 2"

# 1. Print type of vars
print(type(X))
print(type(Y))

# 2. Vilken datatyp har variablen adresses?
print(type(addresses))

#3. Få ut Bellas adress
print(addresses["Bella"])

#4 Vad händer när nedan rad skrivs? Objektet läggs till i dict.
addresses["Daniel"] = "Prinsgränd 2"
addresses["Carl"] = "Bygatan 15"

#5 Hur många keys har adresses?
print(len(addresses))

#5.1 Får fram adress sista personen i bokstavsordning. 

sortlist = list(sorted(addresses)) #skapa lista och sortera denna till ny variabel
lastName = sortlist[-1] #tar ut sista värdet i alfabetisk ordning bland "keys" i dict i den sorterade listan alltså namnet och placerar i egen variabel. 
print(addresses[lastName])  #printar värdet ur dictionaryn med hjälp av keyword. 

#5.2 my_dict: my_dict = {v: k for k, v in my_dict.items()} 

addresses_list = list(sorted(addresses.values()))
first_street = addresses_list[0]

addresses : addresses = {v: k for k, v in addresses.items()}
print(first_street)

#6 vilken datatyp har var cars?
print(type(cars))

#7 vad returneras om man skriver cars[x]? // Opel p.g.a. att variabeln X = 1 och opel är värde 1 i listan.
print(cars[X])

#8 Vad returneras om man skriver cars[Y], varför? 
#print(cars[Y])
# IndexError: list index out of range returneras. Y = 4 och det finns bara 3 värden i listan.

#9 Vad returneras om man först skriver cars.sort() och på nästa rad skriver cars[0]? 
cars.sort()
print(cars[0])
# BMW returneras efter att listan blivit sorterad i bokstavsordning.

#10 se PDF
cars_2 = cars
cars.append("Saab")
print(cars)
print(cars_2)
#10.1 Skapa ytterligare en variabel cars_3 som får sina element av cars men som inte påverkas av vad som läggs till i cars.
cars_3 = cars.copy()
#list = list.copy() skapar en kopia av befintl lista och inte bara en referens till den bef. 

#10.2 Utöka variabeln cars så att den innehåller dubbletter av varje bilmärke sorterat i omvänd bokstavsordning.
cars_4 = cars.copy()
cars.extend(cars_4)
cars.sort(reverse=True)
print(cars)

#10.3 ta bort dubletter från en lista
unique_cars = list(dict.fromkeys(cars))
print(unique_cars)

#11 Vilken datatyp har variablerna numbers1 och numbers2? // Det är två "set".
print(type(numbers1))
print(type(numbers2))

#12 Vilka värden finns lagrade i variablerna numbers1 och numbers2?
print(numbers1) #1, 2, 3, 6 
print(numbers2) #2, 3, 4, 7

#13 Vad är snittet (intersection) mellan variablerna numbers1 och numbers2? 
print(numbers1.intersection(numbers2))

#14 Vad är unionen mellan variablerna numbers1 och numbers2?
print(numbers1.union(numbers2))
# Visar alla värden i båda set, men tar bort dubletter.

#15 Vilken är den symmetriska differensen mellan numbers1 och numbers2?
print(numbers2.symmetric_difference(numbers1))
#visar endast värden som INTE finns i båda. 