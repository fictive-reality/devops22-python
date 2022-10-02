# SUM

#Write a program that fulfills the specification:

# Ask the user for a start and stop integer

# Print every integer between start and stop. i.e. start = 1, stop = 5 would print:

# 1
# 2
# 3
# 4  
# Print the sum of all integers i.e

# Sum: 10




num1 = int(input('Write a start number:'))
num2 = int(input('Write a stop number:'))
print('Your start number is:',(num1),'and','your stop number is:',(num2))
print('List with numbers beetwen:',(num1),'and',(num2))

for x in range((num1+1),(num2)):
   print(x)
   
sum = sum(range((num1+1),(num2)))
print('Sum of all numbers in beetwen is:',(sum))



#If you want to sum value use "sum"-funktion. You can sum all in range. 

