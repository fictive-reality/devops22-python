import random


"""
# Exercise 3 Boolean Operations - and, or, not

x = True
y = False
z = True

# 1 Write a expression with Boolean Operations that:
# 1.1 result in True if any of x, y, z is True
result = x or y or z
if result == True: 
    print("1. The thing it's true")
else: print("1. Not true")
# 1.2 result in True if all x, y, z is True
result = x and y and z
if result == True: 
    print("2. The thing it's true")
else: print("2. Not true")

# 1.3 result in False if any of x, y, z is False
result = x or y or z
if result == False: 
    print("3. The thing it's false")
else: print("3. Not false")

# 1.4 result in False if all of x, y, z is False
result =  x and y and z
if result == False: 
    print("4. The thing it's false")
else: print("4. Not false")

# 1.5 result in False if any of z, y, z is True
result =  x or y or z
if result == True: 
    print("5. The thing it's false")
else: print("5. Not false")

# 1.6 result in False if all of z, y, z is True
result =  x and y and z
if result == True: 
    print("6. The thing it's false")
else: print("6. Not false")
"""
"""   
# Exercise 4
# 1 Create a empty list
list = list()

# 2 Create a string that is a color e.g "red"
color = "red"

# 3 Add the color to your list
list.append(color)
# 4 Print the color from the list using Common Sequence Operations indexing for 0 i.e my_list[0]
print(list[0])
# 5 Add two other color to the list
list.append("blue")
list.append("yellow")
print(list)
# 6 Search for a color in the list using operation x in s
if "red" in list:
    print("The list has red")
else:
    print("the list doesn't contain red")

check_list = [x for x in list if "red" in x] 
print(check_list)   
# 7 Verify that a color is not in the list using the operation x not in s
check_list = [x for x in list if "green" in x]
print(check_list)
# 8 Create another list of colors and concatenate the two lists using the operation s + t
extra_colors = ["green", "pink", "black"]
print(f"The second list {extra_colors}")
list = list + extra_colors
print(f"The new big list {list}")
# 9 Create a list of two colors red, yellow with three of each color using the operation s * n
double_list = ["red", "yellow"]
double_list = double_list * 2
print(double_list)

# 10 Print the first four colors in the list from (9) using the operation s[i:j]
print(double_list[0:4])

# 11 Count how many times "red" occur in the list using the operation s.count(x)
list.append("red")
counter = list.count("red")
print(f"Color red appears {counter} times")
# 12 Print the index of the first occurrence of "yellow" in s using the operation s.index("yellow")
first_index = list.index("yellow")
print(f"the first occurence of yellow it's at index {first_index}")

# 13 Print the total length of each array using the operation len(s)
l1 = len(list)
l2 = len(double_list)
print(f"The lenght of first list it's {l1} and of the second list {l2}")
# 14 Create a list of 7 numbers
random_list = random.sample(range(1, 99), 7)
print(f"The random list: {random_list}")

# 14.1 Print the min value in the list
minim = min(random_list)
print(f"The smallest number in the list is {minim}")
# 14.2 Print the max value in the list
maxim = max(random_list)
print(f"The biggest number in the list is {maxim}")
"""

# Exercise 5 Sorting
# In LINKS_3.md there is a link Python guide how-to do sorting. 
# Create a list containing 10 car brand. i.e cars = ["volvo", ...]
long_car_list = ["Dacia","Lamborghini", "Audi", "Skoda", "Trabant", "Aro", "Mercedes", "Opel", "Citroen", "Renault"]
# Sort the list with sorted(cars)
sorted = sorted(long_car_list)
print(f"The long car list {long_car_list}")
print(f"The first sort of the long car list {sorted}")
# Sort the list with cars.sort()
sorted_2 = long_car_list.sort()
print(f"The second sort of the long car list {long_car_list}")
# reverse the sort of both, read more about reversing in python docs ascending-and-descending
print("The list sorted:")
print(sorted)
# Extra exercise, create a list of 10 tuples containing (brand, model), i.e ("volvo", "xc90"). 
# Sort first on brand, then on model.
print("Tuple list")
tuple_list = [("Dacia", "Logan"), ("Lamborghini", "Diablo"), ("Audi", "A6"), ("Skoda", "Octavia"), ("Opel", "Astra")]
print(tuple_list)
sort_brand = sorted(tuple_list)
sort_model = tuple_list.sort()