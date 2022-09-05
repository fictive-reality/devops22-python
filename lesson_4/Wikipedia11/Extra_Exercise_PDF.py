import random

# -----------------------------Exercise 1-----------------------------
""""
# Write a program that greets the user 10 times

word = "Hello"

for i in range(10):
    print(word)
"""
# -----------------------------Exercise 2-----------------------------

# Write a program with for-loop that prints the following:
#
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

# -----------------------------Exercise 3-----------------------------

"""# while True:
    # word = input("Please enter a word. To stop, enter 'stop': ")
    # if word == "stop":
        # break
    # else:
    #   len_word = len(word)
    #   print(f"The word is {word}, which has {len_word} characters")
    #   print("Enter 'stop' to quit")

while True:
    user_num = int(input("Enter a integer: "))
    if user_num == 74:
        print("Correct")
        break
    elif user_num < 74:
        print("Wrong, it's higher")
    elif user_num > 74:
        print("Wrong, it's lower.")    
"""
# -----------------------------Exercise 4-----------------------------

# Write a program that loops over a list containing different numbers. If the program crashes
# on an uneven number write the words “Not allowed!” out and the loop is terminated.

# Working as intended.
# i found the line "random_index = random.randint(0,len(num_list)-1)" searching on google but i do understand what it does.
# It goes into a module and pulls out a random int which im using as a index for my list, i could even use this module without my list
# for it to be completly random
"""
num_list = [1, 6, 8, 9, 45, 44, 75, 23, 76, 60, 78, 23, 70]
random_index = random.randint(0,len(num_list)-1)

while True:
    num_list = [1, 6, 8, 9, 45, 44, 75, 23, 76, 60, 78, 23, 70]
    random_index = random.randint(0,len(num_list)-1)
    if num_list[random_index] % 2 == 0:
        continue
    else:
        print("Not allowed!")
        break
"""
# -----------------------------Exercise 5-----------------------------

# Using a for loop, write a program that for each number in second_list, retrieves
# the number and its position in first_list and writes the result as a list of tuples.
# Example:

# Output: [(2, 3), (3, 0), (6, 4), (7, 1), (9, 2)]
""""
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
list_1 = list() # Creating a empty list to store all the tuples

i = 0 # THis is the counter, it needs to start a 0

# The program will go on until the counter reaches the same number as there are values in second_list, for this exemple its 5.
# 
while i < len(second_list):
    tuple_1 = (first_list[i], second_list[i]) 
    list_1.append(tuple_1) # Adding the tuples to the list
    i += 1 # Counter goes up by one
print(list_1)
"""
# -----------------------------Exercise 6-----------------------------




# -----------------------------Exercise 7-----------------------------




# -----------------------------Exercise 8-----------------------------




