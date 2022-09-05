# IF
## Python Program to Check if a Number is Odd or Even

num = int(input('Write a number: '))
print('You wrote a number that is:', (num))
if num % 2 == 0:
    print('{0} is even '.format(num))
else:
    print('{0} is odd'.format(num))

### A number is even if it is perfectly divisible by 2. 
### When the number is divided by 2, we use the remainder operator % to compute the remainder. 
### If the remainder is not zero, the number is odd.    
