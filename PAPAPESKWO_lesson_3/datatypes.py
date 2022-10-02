from multiprocessing.sharedctypes import Value


X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

addresses["Daniel"] = "Prinsgränd 2"
print (addresses["Daniel"])

print(len(addresses))

result = sorted(addresses.keys())
#addresses.keys kommer ge namn. .items ger namn och address
print(result[-1])

my_dict = {value: key for key, value in addresses.items()}
faddr = sorted(my_dict.keys())
print(faddr[0])

print(cars[X])

#print(cars[Y])

cars.sort()
print(cars[0]) 

cars_2 = cars

cars_2.append("Saab")
#med append lägger vi till Saab i cars
print(cars)

cars_3 = tuple(cars)
print(cars_3)

cars = cars *2
cars.sort(reverse = True)
print(cars)

unique_cars = cars
print(unique_cars)
#slice operator :: (start:end:step)

#cars = []
#skapar en ny lista
#[cars.append(z) for z in unique_cars if z not in cars] 
#print(cars)

unique_cars = set(cars)
#set kan endast ha unika värden
print(unique_cars)

z = numbers1.intersection(numbers2)
print(z)
#13

uni = numbers1.union(numbers2)
print(uni)
#14

sd = uni = numbers1.symmetric_difference(numbers2)
print(sd)


#1 int
#2 Dictionary
#3 print (addresses["Bella"])
#4 sparat value/string "prinsgränd 2" med keyen daniel
#5 print(len(addresses))
#5.1 result = sorted(addresses.keys())
#     print(result[-1])
#5.2 my_dict = {value: key for key, value in addresses.items()}
#    faddr = sorted(my_dict.keys())
#    print(faddr[0])
#6 list
#7 Opel
#8 För värdet är större än antal strings i listan. En femte string finns ej i listan
#9 BMW. den sorterar strängarna i bokstavsordning och skriver sedan ut den första
#10 Den refererar tillbaka. En låda med fyra bilar och två etiketter
#10.1 cars_3 = tuple(cars)
#10.2 cars = cars *2
#     cars.sort(reverse = True)
#     print(cars)
#10.3 unique_cars = cars[::2]
#     print(unique_cars)
#11 De har SET
#12 INT
#13