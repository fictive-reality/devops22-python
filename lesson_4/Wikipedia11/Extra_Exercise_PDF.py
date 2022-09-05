import random
from re import X
from tkinter import N

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
# for loop med range, printa med string *n
""""
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 0

for n in num_list:
    print((str(n) * n))
    n += 1
#print(str(number * str(i)))
"""
# -----------------------------Exercise 3-----------------------------
"""
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

# SKipping this for now
# Might give it a go later

# -----------------------------Exercise 7-----------------------------

# You have the following list of fruits:
# fruit = ['apple', 'orange', 'pear', 'banana', 'grapes']
# Write a program that asks the user by how many slots for fruit he has in his
# basket, and then you fill this basket (a list) with fruits by looping through
# the fruit list until the basket list is full.
# Output example:
# My_basket = ['apple', 'orange', 'pear', 'banana', 'grapes', 'apple',
# 'orange', 'pear']
"""
fruit = ['apple', 'orange', 'pear', 'banana', 'grapes']
fruit_list = list()
slots = int(input("How many slots for fruits do you have in your basket? "))

i = 0
while True:
    if i <= slots:
        fruit_list.append(fruit[i % 5]) # The answer was infront of me the whole time, modulo operator solved it.
        i += 1
    else:
        print(f"Your basket is full\nIt contains {fruit_list}")
        break
"""
# -----------------------------Exercise 8-----------------------------

# Write a program that uses nested while loops to print all prime numbers
# which is less than 100.
# Guidance: A prime number is a number that is greater than 1 and cannot be evenly divided by
# any number other than itself and 1. See wikipedia for how to calculate what is one
# primes: https://sv.wikipedia.org/wiki/Primes
# Examples of prime numbers are 2, 3, 5, 7, 11, 13, 17 and 19
# 4, 6, 8, 9, 10, 12, 14, 15, 18 and 20 are not prime numbers (because eg 20/ 5 = 4, 14/7 = 2 etc.)
"""
prim_tal = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

i = 0
j = 0

while True:
    if i in prim_tal:
        print(prim_tal[j])
        j += 1
    i += 1
"""

# Not my solution, i just copied it to figure it out.

""""
primes = []
p = 2

while p < 100:
    n = 2 
    while p%n != 0:
        n += 1
    if (n == p):
        primes.append(p)
    p += 1
print(primes)
"""