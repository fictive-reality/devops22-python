import random

# 1. Skriv ett program som hälsar användaren 10 gånger.
print("Problem 1")
print("-----------------")
# 2. Skriv ett program (med for-loop) som skriver ut följande:
print("Problem 2")
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
random_list = random.sample(range(1, 99), 7)
print(random_list)
while True:
    if i in random_list(i) % 2 != 1:
        print("Not allowed!")
        break
print("-----------------")
# 5. Genom att använda en for-loop, skriv ett program som för varje tal i second_list, hämtar talet och dess position 
# i first_list och skriver resultatet som en lista av tupler.

print("Problem 5")
print("-----------------")
# 6. Upprepa uppgiften ovan, men använd denna gång list comprehension för att lösa problemet.
print("Problem 6")
print("-----------------")
# 7. Du har följande lista på frukter:
fruits = ['apple', 'orange', 'pear', 'banana', 'grapes']
#Skriv ett program som frågar användaren efter hur många platser för frukt hen har i sin korg,
# och sedan fyller du denna korg (en lista) med frukter genom att loopa igenom frukt-listan tills dess 
# att korg-listan är full.

print("Problem 7")
print("-----------------")
# 8. Skriv ett program som använder sig av nästlade while-loopar för att skriva ut alla primtal som är mindre än 100.

print("Problem 8")
print("-----------------")