from operator import itemgetter
from re import A


my_cars = ["volvo", "volkswagen", "BMW", "mercedes", "Opel", "Aston Martin", "Jeep", "Audi", "renault", "toyota"]

sorted(my_cars)
print(my_cars) # sorted(my_cars) gör i mina ögon ingenting?, varför är det så?

my_cars.sort()
print(my_cars) # med my_cars.sort() blir det sorterat efter första bokstaven..  Får googla och kolla på varför

# Nu är jag med! sorted() ändrar inte den ursprungliga list:en. Därför ser jag inte skillnaden när jag lägger print() efter åt

print(sorted(my_cars))
print(my_cars)

#print(sorted(my_cars, reverse=True))
my_cars.sort(reverse=True)
print(my_cars)

# sorted() för att inte göra en permanent ändring.
# list.sort() för att göra en permanent ändring

tuple_volvo = ("Volvo", "xc90")
tuple_bmw = ("BMW", "330i")
tuple_VW = ("VW", "Golf")
tuple_opel = ("Opel", "Astra")
tuple_mercedes = ("Mercedes", "A45")
tuple_audi = ("Audi", "RS6")
tuple_mini = ("Mini", "Copper")

new_car_list = list()
new_car_list.extend([tuple_audi, tuple_bmw, tuple_mercedes, tuple_mini, tuple_opel, tuple_VW, tuple_volvo])
print(new_car_list)

print(sorted(new_car_list))
# För att sortera på model så måste key=itemgetter(1) skrivas med. key=itemgetter är en inbyggd modul i python
# som för list like object callable, se nedan
#
# operator is a built-in module providing a set of convenient operators. In two words operator.itemgetter(n) constructs a callable that assumes an iterable 
# object (e.g. list, tuple, set) as input, and fetches the n-th element out of it.

print(sorted(new_car_list, key=itemgetter(1)))