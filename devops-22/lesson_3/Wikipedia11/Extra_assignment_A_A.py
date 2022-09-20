from audioop import add
import collections
from enum import unique
import operator
from operator import itemgetter
from collections import OrderedDict

X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5", "Bella": "Klockgatan 1", "Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]


#print(addresses["Bella"])
addresses["Daniel"] = "Prinsgränd 2"
#print(addresses)

# Fråga 1: Int
# Fråga 2: Dict
# Fråga 3: adresses["Bella"]
# Fråga 4: Man lägger till "Daniel": "Prinsgräns 2"
# Fråga 5
print(type(addresses))
 
from_dict_to_list = list(addresses)
print(from_dict_to_list[-2])

(print(type(from_dict_to_list)))

 
#print(list(addresses))
# print(sorted(addresses))

# addresses = {k: v for k, v in sorted(addresses.items(), key=lambda item: item[1])}
# print(list(addresses))

#addresses = {v: k for k, v in addresses.items()}
#print(addresses)
#print(sorted(addresses.values()))
sorted(addresses.values())
print(type(addresses))

addresses = {v: k for k, v in addresses.items()}
print(list(sorted(addresses)))


#sorted(addresses.items(), key=itemgetter(1))
#print(type(addresses))
#print(addresses)

#print(OrderedDict(sorted(addresses.items(), key = itemgetter(1))))


# Fråga 6
# Det är en list
#print(type(cars))

# Fråga 7
# Andra värdet i listen kommer att retuneras, dvs Opel
print(cars[X])

# Fråga 8
# Inget värde kommer att returneras då endast värde 0, 1 och 2 finns i listen

#print(cars[Y])

# Fråga 9
# BMW kommer att retuneras för det som händer i cars.sort() är att man sorterar listen

(cars.sort())
print(cars[0])

# Fråga 10

# Jag har ingen aning om det är är rätt..? Men båda variablarna innehåller nu "Saab".
# Anledning är för att cars_2 är kopplad till cars, så allt som läggs in i cars kommer till cars_2
# Tjuvlyssnade på när Martin förklarade detta problemet för någon annan
# Och det man ska göra står inte utskrivet i PDF:en
# Men måste se till så att den nya variabeln pekar på den orginala listan och inte variablen
# Då förblir den som listan är

cars = ["Volvo", "Opel", "BMW"]
cars_2 = list(cars)
cars.append("Saab")
cars_3 = list(cars)
print(cars)
#cars.append("Volvo", "Opel", "BMW")
print(cars)

# unique_cars = cars
unique_cars = list(dict.fromkeys(cars))
print(unique_cars)


# Fråga 11
# Dom är set

numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

print(type(numbers1))
print(type(numbers2))

print(numbers1)

# Fråga 12
# numbers1 = 1, 2, 3, 6
# numbers2 = 2, 3, 4, 7

# Fråga 13
# Intersection returnar det som båda seten innehåller, i detta fallet 2 & 3
intersection = numbers1.intersection(numbers2)
print(intersection)

# Fråga 14
# union slår ihop båda variablerna men tar bort dubletter
# 1 2 3 4 6 7 
union_x = numbers1.union(numbers2)
print(union_x)

# Fråga 15
# symmetric_difference visar värdena som skiljer variablarna åt
# 1 4 6 7 
sys = numbers1.symmetric_difference(numbers2)
print(sys)

