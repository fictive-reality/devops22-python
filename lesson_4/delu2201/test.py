from operator import index
from re import S
#Övning 5

first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
my_list = []
#my_tuple = {}
for x in range(0, len(second_list)):
    temp_var = second_list[x]
    temp_var_igen = first_list.index(temp_var)
    #print(f" {temp_var} {first_list.index(temp_var)}")
    my_tup = (temp_var, first_list.index(temp_var))
    my_list.append(my_tup)
#print(first_list.index(temp_var))
#print(my_tup)
print(my_list)