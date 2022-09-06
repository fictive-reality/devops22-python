from copy import copy, deepcopy
import itertools
from sys import builtin_module_names

X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}

cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}
#print (f' addresses ["Bella"]:{addresses["Bella"]}')

addresses ["Daniel"] = "Prinsgränd 2"

#print(f'{len(addresses)}')

#print (list (addresses.items())[-1][1])

#addresses : addresses = {v: k for k, v in addresses.items() }

#print (sorted (addresses)[0])
cars.sort()
#print (cars [0])
#cars_2 = cars 
#cars.append("Saab")
#cars_3 = copy(cars)
#cars_3.pop()
#print (cars,cars_2,cars_3)

colors = []
färg1 = "green"
colors.append(färg1)
#print (colors [0])
färg2 = "blue"
färg3 = "red"
colors.extend([färg2, färg3])
#print ("red" in colors)
#print ("yellow" in colors)
#print (colors)
colors_2 = ["purple", "orange", "pink"]
colors_3 = colors + colors_2
#print (colors_3)

redyel_list = 3 * ["red ","yellow "]
#print (redyel_list[0:4])
#print (redyel_list.count("red "))
#print (redyel_list.index("yellow "))
#print (len(redyel_list))

numlist = [3,7,2,6,8,4,9]
#print (min(numlist), max(numlist))

carlist = [("Tesla", "Model s"), ("Ferrari","F8"), ("Audi", "R8"), ("Volvo", "Amazon"), ("Bmw", "M8"), ("Mercedes", "AMG")
, ("Opel", "Rekord"), ("Toyota", "GR supra"), ("Porsche", "Cayman"), ("Jaguar", "F-Type")]
#carlist.sort(reverse= True)
#print (sorted (carlist))
#sortedcarlist = sorted(carlist, reverse=True)
#print (sortedcarlist)
carlist.sort()
print (carlist)
