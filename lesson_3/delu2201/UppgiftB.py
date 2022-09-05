person1name = "Bertil" #input("Mata in första personens namn: ")
person1age =  30 #input("Mata in första personens ålder: ")
person1shoe = 12 #input("Mata in första personens skostorlek: ")

#person1data = {person1name: (person1age, person1shoe)}

person2name = "Ceasar" #input("Mata in andra personens namn: ")
person2age = 20 #input("Mata in andra personens ålder: ")
person2shoe = 15 # input("Mata in andra personens skostorlek: ")

#person2data = {person2name: (person2age, person2shoe)}

person3name = "Adam" #input("Mata in tredje personens namn: ")
person3age =  10 # input("Mata in tredje personens ålder: ")
person3shoe = 18 #input("Mata in tredje personens skostorlek: ")

#person3data = {person3name: (person3age, person3shoe)}

#person1data.update(person2data)
#person1data.update(person3data)

persondata = {person1name: (person1age, person1shoe), person2name: (person2age, person2shoe), person3name: (person3age, person3shoe)}
print(persondata)

oldest = sorted(persondata, key=lambda student: student[1])
print(oldest)

print(type(oldest))

