#Repeat word

#Write a program that fulfills the specification:

# Ask the user for a word

# Print the word x times, where x = len(word). i.e if the word is hello the program writes:

# hello
# hello
# hello
# hello
# hello

from timeit import repeat


repeat_word = (input('Write a word:  '))
print('Yot wrote word:', (repeat_word)) 
#Printing repeat_word X times, where x=len(word)
x = repeat_word 
for x in range(0,len(repeat_word)):
   print(repeat_word) 
     
 

# range(0, len(X)) is about "from and until". You need to define X to repeat same value several times. 