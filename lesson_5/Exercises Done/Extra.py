""" Extra

Write a program that handles salary negotiations. The user is the employee and the boss is your program.

The boss tells the user it's current salary and currency
The employee ask for more money with an input. I.e 2000 more
The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
The employee ask again for another amount i.e 1800
The boss calculates the percentage and respond yes or no, you decide which criteria the boss uses. 
4 and 5 iterates in a loop until the employee quit or the boss accept the amount. 
"""
salary = int('2000')
print(f'Boss: "Your current salary is:" \u20AC{salary}')
more = int(input(f'Enployee: "I want more:" \u20AC'))
percentage = more/salary*100

while salary == salary:
    print(f'Boss:"You are asking for {percentage}% more in salary. My answer is NO \N{sneezing face}')
    
    answer = input(str('Do you want to continue?:'))
    break

while True:
   if answer.lower().startswith("y"):
      print("ok, carry on then")
      more = int(input(f'Enployee: "I want more:" \u20AC'))
      
   else:
        answer.lower().startswith("n")
        print("ok, sayonnara")
        exit()

   if more > int('399'):
        percentage = more/salary*100
        print(f'Boss:"You are asking for {percentage}% more in salary. My answer is NO \N{sneezing face}')
        answer = input(str('Do you want to continue?:'))
        
   else:
         more < int('399')
         print(f'Boss:"You are asking for {percentage}% more in salary. My answer is YES \N{winking face}')
         break  










""" 
while more > int('399'):
    percentage = more/salary*100

    print(f'Boss:"You are asking for {percentage}% more in salary. My answer is NO \N{sneezing face}')
    
    more = int(input(f'Enployee: "I want more:" \u20AC'))    
else:
    percentage = more/salary*100
    print(f'Boss:"You are asking for {percentage}% more in salary. My answer is YES \N{winking face}')

 """