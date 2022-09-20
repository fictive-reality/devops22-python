from operator import itemgetter
from re import search




# Input till person 1

person_1_name = "fredrik".title() #input("Please enter name for person 1: ").title
person_1_age = 30 #input("Please enter age for person 1: ")
person_1_shoesize = 40 #input("Please enter shoesize for person 1: ")
person_1 = (person_1_name, person_1_age, person_1_shoesize)

# Input till person 2
person_2_name = "johanna".title() #input("Please enter name for person 2: ").title
person_2_age = 28 #input("Please enter age for person 2: ")
person_2_shoesize = 39 #input("Please enther shoesize for person 2: ")
person_2 = (person_2_name, person_2_age, person_2_shoesize)

# Input till person 3
person_3_name = "patrik".title() #input("Please enter name for person 3: ").title
person_3_age = 45 #input("Please enter age for person 3: ")
person_3_shoesize =  42 #input("Please enther shoesize for person 3: ")
person_3 = (person_3_name, person_3_age, person_3_shoesize)

persons = [(person_1_name, person_1_age, person_1_shoesize), (person_2_name, person_2_age, person_2_shoesize), 
(person_3_name, person_3_age,person_3_shoesize)]

# I raden nedan så sorteras persons på andra positionen (age i detta fallet) och väljer en position, i detta fallet första bakifrån [-1] att
# spara i variabeln oldest
oldest = sorted(persons, key=lambda person: person[1])[-1]

print(f"{oldest[0]} is the oldest with a shoe size of {oldest[2]}.")

shoe_size = sorted(persons, key=lambda person: person[2])[1]

print(f"{shoe_size[0]} is the person with median shoe size and is {shoe_size[1]} years old")

search_input = input("Please define a search value: ")
