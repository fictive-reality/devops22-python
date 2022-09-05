#Exercise 5 Until stop
# 
# Write a program that fulfills the specification: --> --> --> -->

# Create a while loop that runs forever
# In each iteration, input a text
# In each iteration, print a text "Enter stop to quit: "
# If the text equals stop, break the while loop
# If the text don't equals stop, print the text and the length of the text
# 

x = str(input('Write a short text:'))
y = str("stop").lower()
while x != y:
    print('Your wrote this text:',(x))
    print('Lenght of the text is:',len(x),'signs')
    x = str(input('Enter stop to quit:'))
    
# this you can use when values are "wrong and you need to ask person again same question"
