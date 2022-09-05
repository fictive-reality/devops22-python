#Övning 2

from email import iterators


iterations = 2
number = 2
#while iterations < 9:
for x in range(8):
    print(f" {str(number) * iterations}")
    x += 1
    number +=1
    iterations +=1

