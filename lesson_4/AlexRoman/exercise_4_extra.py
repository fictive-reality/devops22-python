"""
import random

# 1. Skriv ett program som hälsar användaren 10 gånger.

print("Problem 1")
salut = input("Please enter your name: ").capitalize()
print(f"Variant 1: Welcome {salut * 10}")
print("Variant 2: ")
for i in range(10):
    print(f"Welcome {salut}")
print("-----------------")

# 2. Skriv ett program (med for-loop) som skriver ut följande:
print("Problem 2")
for i in range(10):
    print(f"{str(i) * i}")
print("-----------------")

# 3. Skriv ett program som låter användaren gissa vilket tal du tänker på tills användaren gissar rätt.
#T alet har du hårdkodat in i programmet och gissningen från användaren hämtas in via input gång på gång 
# tills dess att gissning == input.

print("Problem 3")    
random_number = random.randrange(0, 99)
print(f"The random number is {random_number} just in case you panic")
while True:
    guess = int(input("Guess my number, between 0 and 99: "))
    if (guess == random_number):
        print("You did it!")
        break
    elif (guess < random_number):
        print("Wrong, it's higher. Try again")
    elif (guess > random_number):
        print("Wrong, it's lower. Try again")
print("-----------------")

# 4. Skriv ett program som loopar över en lista innehållandes olika tal. Om programmet stöter på ett ojämnt tal skrivs 
# orden “Not allowed!” ut och loopen avbryts.

print("Problem 4")
random_list = random.sample(range(1, 99), 7) # for testing with a random list
print(random_list)
not_random_list = [1, 3, 5, 7, 9, 11, 13]
print(not_random_list)
for x in not_random_list:
    if x % 2 != 1:
        print("Not allowed!")
        break
    else:
        print(x)
print("-----------------")

# 5. Genom att använda en for-loop, skriv ett program som för varje tal i second_list, hämtar talet och dess position 
# i first_list och skriver resultatet som en lista av tupler.

print("Problem 5")
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
tuple_list = []

for x in second_list:
    if x in first_list:
        y = first_list.index(x)
        tuple_xy = (x, y)
        tuple_list.append(tuple_xy)
print(tuple_list)        
print("-----------------")

# 6. Upprepa uppgiften ovan, men använd denna gång list comprehension för att lösa problemet.

print("Problem 6")
first_list = [3, 7, 9, 2, 6]
second_list = [2, 3, 6, 7, 9]
newlist = []

for x in second_list:
    if x in first_list:
        y = first_list.index(x)
        tuple_xy = (x, y)
        newlist.append(tuple_xy)
        
print(newlist)
print("-----------------")

# 7. Du har följande lista på frukter:
# fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
# Skriv ett program som frågar användaren efter hur många platser för frukt hen har i sin korg,
# och sedan fyller du denna korg (en lista) med frukter genom att loopa igenom frukt-listan tills dess 
# att korg-listan är full.

print("Problem 7")
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
basket = list()
empty_slots = int(input("How many slots do you have in your basket? "))
i = 0
while True:
    if i < empty_slots:
        basket.append(fruits[i % 5])
        i += 1
    else:
        print(f"Your basket is filled with {empty_slots} items and contain this fruits : {basket}")
        break
print("-----------------")
"""
# 8. Skriv ett program som använder sig av nästlade while-loopar för att skriva ut alla primtal som är mindre än 100.

print("Problem 8")
prime = []
for number in range(1, 101):
    if( number > 1):
        for i in range(2,number):
            if (number % i) == 0:
                break
        else:
            prime.append(number)
print("The prime numbers under 100 are: ")
print(prime)
print("-----------------")


# 8 Solved in class
print("Problem 8 Variant 2 Solved in class")
prime2 = []
i = 1
while i < 100:
    i += 1
    j = 2
    while j < i:
        if i % j == 0:
            break
        j += 1
    else:
        prime2.append(i)
        # print(i)
print(prime2)
print("-----------------")