from typing import Concatenate

# Exercise 4

#1
list_builtin = list()

#2
colors = "red"

#3
list_builtin.append(colors)

#4
print(list_builtin[0])

#5
list_builtin.append("green")
list_builtin.append("purple")

#6
print("purple" in list_builtin)

#7
print("yellow" not in list_builtin)

#8
my_second_list = ["yellow", "white", "blue", "orange"]
#list_builtin.extend(my_second_list)
#print(list_builtin)
my_third_list = list_builtin + my_second_list
print(my_third_list)

#9
my_forth_list = (["red", "yellow"] * 3)
print(my_forth_list)

#10
print(my_forth_list[0:4])

#11
print(my_forth_list.count("red"))

#12
print(my_forth_list.index("yellow"))

#13
print(len(my_forth_list))

#14
# Detta är definitivt inte det rätta tänka sättet att göra det på..
# Jag googlar nu och skriver in det rätta.

my_number_list = [35, 72, 48, 29, 95, 13, 4]
print(min(my_number_list))
print(max(my_number_list))
#my_number_list.sort()
#print(my_number_list[0])
#print(my_number_list[6])
