from sqlite3 import SQLITE_CREATE_VTABLE
from tkinter import W

#Excercise 1

#Ask user for a integer
number = int(input("Ange ett heltal: "))

#Kontrollera om heltal är jämnt
"""Kontrollen görs genom att kontrollera ifall slutprodukten är noll eller ej:
slutprodukt = 0 så är talet jämt
slutprodukt != 0 så är talet udda. """
if number % 2 == 0:
    print("Ditt angivna heltal är jämnt.")
else:
    print("Ditt angivna heltal är udda.")

#Excercise 2

#Ask user for a name.
name = input("Ange ett namn: ").strip().capitalize()

#Skapa en tuple med 5 namn
name_tuple = {"Dennis", "Adam", "Jessica", "Bertil", "Morgan"}

#Kontrollera om angett namn finns med i tuple.
if name in name_tuple:
    print(f"Welcome {name} you are on the list.")
else:
    print(f"Sorry, you are not on the list.")

#EXCERCISE 3

#Ask user for a word
word = input("Please input any word. ")

#extract number of chars in word
number_of_char = len(word)
#Print the word as many times as there are chars in word.

for x in range(number_of_char):
    print(word)
    x += 1

#EXCERCISE 4

#Ask user for start and stop value.
start_value = int(input("Please enter a start value: "))
stop_value = int(input("Please enter a stop value:"))

sum = 0 #Var for holding sum of all numbers

for x in range(start_value, stop_value):
    print(x)
    sum = sum + x
print(f"The sum of all numbers between {start_value} and {stop_value} is {sum}.")