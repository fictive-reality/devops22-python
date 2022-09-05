from audioop import reverse
from operator import itemgetter
#Get 3 persons name, age, shoesize from input.

person1name = "bertil" #input("Mata in första personens namn: ").lower().strip()
person1age = 30 #int(input("Mata in första personens ålder: ").strip()
person1shoe = 40 #float(input("Mata in första personens skostorlek: ").strip()

person2name = "Ceasar" #input("Mata in andra personens namn: ").lower
person2age = 15 #int(input("Mata in andra personens ålder: ")
person2shoe = 21 # float(input("Mata in andra personens skostorlek: ")

person3name = "Adam" #input("Mata in tredje personens namn: ")
person3age = 10 # int(input("Mata in tredje personens ålder: ")
person3shoe = 18 #float(input("Mata in tredje personens skostorlek: ")

#Put all persons info in list of tuples.
persondata = [(person1name, person1age, person1shoe), (person2name, person2age, person2shoe), (person3name, person3age, person3shoe)]

#Sort using function Itemgetter.
sort_oldest = sorted(persondata, key=itemgetter(1), reverse=True)
sort_biggest_shoe = sorted(persondata, key=itemgetter(2))

#extract the oldest persons and biggest (median) shoes info. 
oldest = sort_oldest[0]
shoe = sort_biggest_shoe[1]

# Print info to user.
print(f"The oldest person is {oldest[0].capitalize()} who has shoe size {oldest[2]}.")
print (f"The person with the median shoesize is {shoe[0].capitalize()} who is {shoe[1]}.")
print("Please enter search value, name, age or size followed by value.")

print(sort_oldest)
print(sort_biggest_shoe)

