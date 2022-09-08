# VIP
##Write a program that fulfills the specification:

#Ask the user for a name
#Create a tuple with at least five names
#If the user input is in the tuple, print the text "Welcome {name} your are on the list".
#If the user input is not in the tuple, print "Sorry, you are not on the list".




vip_list = ('Pavel', 'Daniel','Martina','Gregor','Michaela')
name = input('What is your name? Write it here:  ')
if name in vip_list:
    print('Welcome', (name), 'you are on the list!')
else: 
    print('"Sorry, you are not on the list"')


#Examples
 # Check if element 34 exists in tuple
    # if 34 in tupleObj:
        # print("Element Found in Tuple")
    # else:
        # print("Element not Found in Tuple")    
    
    # Check if element 1001 doesn't exists in tuple    
    # if 1001 not in tupleObj:
        # print("Yes, element Not In tuple")
    # else:
        # print("Element is in Tuple")    

