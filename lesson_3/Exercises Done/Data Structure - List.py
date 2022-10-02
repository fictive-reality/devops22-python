# Data Structure - List

# Create a empty list
# Create a string that is a color e.g "red"
# Add the color to your list
# Print the color from the list using Common Sequence Operations indexing for 0 i.e my_list[0]
# Add two other color to the list
# Search for a color in the list using operation x in s
# Verify that a color is not in the list using the operation x not in s
# Create another list of colors and concatenate the two lists using the operation s + t
# Create a list of two colors red, yellow with three of each color using the operation s * n
# Print the first four colors in the list from (9) using the operation s[i:j]
# Count how many times "red" occur in the list using the operation s.count(x)
# Print the index of the first occurrence of "yellow" in s using the operation s.index("yellow")
# Print the total length of each array using the operation len(s)
# Create a list of 7 numbers
# Print the min value in the list
# Print the max value in the list

my_list = []
color = a = "black"
my_list.append(a)
print(f'The color from the list is: {my_list[0]}')
print(f'Adding two more colors to the list')
color = b = "green"
color = c = "orange"
my_list.append(b)
my_list.append(c)
print(f'The colors in the list are: {my_list}')
color = input(f'Please, type wich color are you searching for: ')
if color in my_list:
   print(f'Yes, this color in the list!')
else:
   print(f'Sorry, this color is not in the list...')
my_list2 = ['grey','brown','blue']
my_list3 = my_list + my_list2
special_color = ["red","yellow"]
special_color2 = special_color*3
my_list4 = my_list3 + special_color2
print(f'List with special colors with three of each color is: {special_color2}')
print(f'My new list after adding some new colors include: {my_list4}')
print(f'The first 4 colors in list are: {my_list3[0:4]}')
print(f'"Red" occur in the list: {my_list4.count("red")}')
print(f'The index of the first occurrence of "yellow": {my_list4.index("yellow")}')
print(f'Total length of each array in the lists: {len(my_list)}, {len(my_list2)}, {len(my_list3)}, {len(special_color2)}, {len(my_list4)}')

list_numbers = [10,20,30,40,50,60,70]
print(f'List includes numbers: {list_numbers}')
print(f'Min value in the list is: {min(list_numbers)}')
print(f'Max value in the list is: {max(list_numbers)}')
