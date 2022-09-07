#####################################################################################################
#  Exercise 3 Repeat word                                                                           #
#   Write a program that fulfills the specification:                                                #
#   1. Ask the user for a word                                                                      #
#   2. Print the word x times, where x = len(word). i.e if the word is hello the program writes:    #
#####################################################################################################


word = input("Enter a word: ")
x = len(word)
print(f"I will write your word as many times as the amount of leters in the word")
for i in range(x):
    print(word)