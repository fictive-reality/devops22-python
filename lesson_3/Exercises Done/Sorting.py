#Sorting

# In LINKS_3.md there is a link Python guide how-to do sorting. Create a list containing 10 car brand. i.e cars = ["volvo", ...]

# Sort the list with sorted(cars)
# Sort the list with cars.sort()
# reverse the sort of both, read more about reversing in python docs ascending-and-descending
# Extra exercise, create a list of 10 tuples containing (brand, model), i.e ("volvo", "xc90"). Sort first on brand, then on model.

cars = ["volvo","mercedes","volga","toyota","lexus","renault","ford","kia","bmw","audi"]
print(f'Sorting cars: {sorted(cars)}')
cars.sort()
print(f'List with cars: {cars}')
#
print(f'Sorting cars (in Descending): {sorted(cars,reverse=True)}')
cars.sort(reverse=True)
print(f'List with cars (in Descending): {cars}')

# Note: The simplest difference between sort() and sorted() is: 
# sort() changes the list directly and doesn't return any value, 
# while sorted() doesn't change the list and returns the sorted list.

# Sort with custom function using key
# If you want your own implementation for sorting, the sort() method also accepts a key function as an optional parameter.
# Based on the results of the key function, you can sort the given list.

# list.sort(key=len)

# Alternatively for sorted:

# sorted(list, key=len)

print(f'Sorting cars with key: {sorted(cars,key=len)}')
cars.sort(key=len)
print(f'Sort list with key:{cars}')

cars2 = [("volvo","xc90"),("mercedes","190D"),("volga","mk2"),("toyota","rmb2"),("lexus","v70"),("renault","DYW110"),("ford","gtx"),("kia","lsg30"),("bmw","rtx70"),("audi","xfg40")]
print(f'New list with cars ("brand" and "model"): {cars2}')
# using key= and lambda. Can do both with x.sort and sorted.x
sorted_on_brand = sorted(cars2,key=lambda tup:tup[0])
print(f'List sorted on brand: {sorted_on_brand}')

sorted_on_brand = sorted(cars2,key=lambda tup:tup[1])
print(f'List sorted on model: {sorted_on_brand}')

#Using itemgetter from import  - the simpler way 
from operator import itemgetter
sorted(cars2,key=itemgetter(0,1))
print(cars2)


# using def
def model(x):
    return x[1]

sorted(cars2, key=model)
print(cars2)




