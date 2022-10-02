#1
#print 1-100
lst = list(range(1,101))
print(lst)    

#print even numbers between 2-60
""" 
myList = list(range(2,61))
evensList = [x for x in myList if x % 2 == 0]
print(evensList) """

for number in range(2, 61, 2):
    print(number)

#print odd numbers between 1-77
""" 
myList = list(range(1,78))
evensList = [x for x in myList if x % 2 == 1]
print(evensList) """

for number in range(1, 77, 2):
    print(number)
