from operator import itemgetter

#Get 3 persons name, age, shoesize from input.

person1name = "Bertil" #input("Mata in första personens namn: ")
person1age = 30 #int(input("Mata in första personens ålder: ")
person1shoe = 20 #intinput("Mata in första personens skostorlek: ")

person2name = "Ceasar" #input("Mata in andra personens namn: ")
person2age = 15 #int(input("Mata in andra personens ålder: ")
person2shoe = 21 # int(input("Mata in andra personens skostorlek: ")

person3name = "Adam" #input("Mata in tredje personens namn: ")
person3age = 10 # int(input("Mata in tredje personens ålder: ")
person3shoe = 18 #int(input("Mata in tredje personens skostorlek: ")

#Put all persons info in list of tuples.
persondata = [(person1name, person1age, person1shoe), (person2name, person2age, person2shoe), (person3name, person3age, person3shoe)]
persondata2 = list.copy(persondata)
#print(persondata2)

#Sort using Lambda function and keys
sort_oldest = sorted(persondata, key=itemgetter(1))
sort_biggest_shoe = sorted(persondata2, key=itemgetter(2))

#extract the oldest persons and biggest shoes info. 
oldest = sort_oldest[0]
#print(f"The oldest person is " + oldest[0] + " who has shoe size " + oldest[2] + ".")
#print (f"The person withe the median shoesize is " + biggest_shoe[0] + )

print(sort_oldest)
print(sort_biggest_shoe)
#print(biggest_shoe)
#print(oldest[0])

#print(type(oldest))

