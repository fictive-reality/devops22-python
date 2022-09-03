X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
"Bella": "Klockgatan 1", "Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"] 
numbers1 = {1, 2, 3, X, 6} 
numbers2 = {Y, 2, 3, 4, 7}


# 1 Vilken datatyp har variablerna ​X​ och ​Y​? int fixed
print("------1-----")
print(f"Variabel 'X' it's of type {type(X)} and variabel 'Y' it's of type {type(Y)}")
print("-----------")
# 2 Vilken datatyp har variabeln ​addresses? ​Dictionary !?
print("------2-----")
print(f"Variable 'addresses' it's of type {type(addresses)}")
print("-----------")
# 3 Hur kan man få ut bellas adress ur variabeln ​addresses?​ Åtkomst till "value" genom "key"
print("-----3------")
b = addresses["Bella"]
print(f"Bella address: {b}")
print("-----------")
# 4 Vad händer om man skriver ​addresses[“Daniel”] = “Prinsgränd 2”?​ Finns inte key Daniel, måste använda () for att deklarera
#addresses[“Daniel”] = “Prinsgränd 2” 
print("-----4------")
print("Daniel it's not declared, must use ()")
print("-----------")
# 5 Få ditt program att skriva ut hur många keys ​addresses​ har.
print("-----5------")
last_index = len(addresses)
print(f"The total number of keys is: {last_index}")
print("-----------")
# 5.1 Utöka programmet så att adressen skrivs ut till den personen som kommer sist i bokstavsordning.
print("-----5.1-----")
last_position = last_index - 1
index_list = list(addresses)
last_name = index_list[last_position]
print(f"The last person name is {last_name}")
print(f"The adress of the last person is: {addresses[last_name]}")
print("-----------")
# 5.2 Utöka programmet så att namnet skrivs ut på den personen som bor på adressen som kommer först i bokstavsordning. 
# ​Tips:​ följande rad byter plats på keys och values i ​my_dict:​
# ​my_dict = {v: k for k, v in my_dict.items()}
print("-----5.2-----")
print("-----------")
# 6 Vilken datatyp har variabeln ​cars?​ List
print("------6-----")
print(f"Variable 'cars' it's of type {type(cars)}")
print("-----------")
# 7 Vad returneras om man skriver ​cars[X]​?  x = 1, cars index 1, second position, Opel
print("------7-----")
print(f" {cars[X]}") 
print("-----------")
# 8 Vad returneras om man skriver ​cars[Y]​, varför? Finns inte index 4 bara 0 till 2
print("------8-----")
print("There is no index 4")
print("-----------")
# 9 Vad returneras om man först skriver ​cars.sort() ​och på nästa rad skriver Sort the list, alphabetic.
print("------9-----")
print(cars)
cars.sort()
print(cars[0])
print(cars)
print("-----------")
# 10 Skapa en ny variabel genom att skriva ​cars_2 = cars​, och på följande rad ska
# strängen ​“Saab”​ läggas till ​cars ​med hjälp av ​append(). ​Notera att det alltså bara är ena variabeln som ska utökas. 
# Vad innehåller variablerna ​cars_2 ​och cars​ nu? Förklara! De innehåller samma index
print("------10-----")
print(f"original cars list {cars}")
cars_2 = cars
print(f"The second list before append {cars_2}")
cars.append("Saab")
print(f"The second list after append {cars_2}")
print(f"the original cars list after append {cars}")
print("-----------")
# 10.1 Skapa ytterligare en variabel ​cars_3​ som får sina element av c​ars men som inte påverkas av vad som läggs till i ​cars.​
print("-----10.1-----")
cars_3 = tuple(cars)
print(f"original cars list {cars}")
print(f"original tuple {cars_3}")
cars.append("Audi")
print(f"the cars list after append {cars}")
print(f"the tuple cars_3 list after append {cars_3}")
print("-----------")


# 10.2 Utöka variabeln ​cars​ så att den innehåller dubbletter av varje bilmärke sorterat i omvänd bokstavsordning.
print("-----10.2-----")
cars = cars + cars
cars.sort()
print(f"cars doubled {cars}")
cars.reverse()
print("cars doubled and reversed:")
print(cars)
print("-----------")


# 10.3 Från den utökade versionen av ​cars ifrån förra uppgiften ,skapa variabeln ​unique_cars ​som ska vara 
# en lista där varje bilmärke finns med exakt en gång.
print("-----10.3-----")
cars.append("Audi")
cars.append("Audi")
cars.append("Opel")
print(f"The car list with a ton of doubles: {cars} ")
unique_cars = set(cars)
print("The unique car list")
print(unique_cars)
print("-----------")