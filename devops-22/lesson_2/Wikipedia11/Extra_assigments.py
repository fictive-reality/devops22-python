from datetime import datetime
from time import time
from xml.etree.ElementTree import PI
import math
from math import sqrt
import time

a = 5
b = a
a = 7
c = a+b

print(c) 



a = 7 * 3 + 1
print(a)




# Uppgiften: Skriv ett program som först ber användaren om tal A, sedan tal B
#   a, Skriv ut summan av de båda talen
#   b, Skriv ut skillnaden mellan de båda talen
#   c, Skriv ut de båda talen multiplicerade med varandra

nummer_a = int(input("Skriv ett tal: "))
nummer_b = int(input("Ge mig ett tal till: "))

print(nummer_a + nummer_b)

if nummer_a > nummer_b:
    diff = nummer_a - nummer_b
else:
    diff = nummer_b - nummer_a

print("Detta är differensen mellan tal 1 och tal 2:",diff)
print("Detta är numrena multiplicerat med varandra:", nummer_a * nummer_b)


# Ta in två tal från användan som i uppgiften ovan och
#   a, använda division för att se vad de olika talen blir delat på varandra
#   b, samma som ovan men med heltalsdivision
# Kommer att använda tidigare variablar för att underlätta för mig själv

print("Divison:",nummer_a / nummer_b)
print("Heltalsdivison:",nummer_a // nummer_b)


# Skriv ett program som tar in radien på en cirkel från användaden och beräknar cirkelns area
# Denna övningen var lite klurig..  fick det att fungera genom att importera 
# en modul (math) då kunde jag använda math.pi för att koden skulle fungera
# Och nu ser jag i PDF filen för denna övning att man ska skriva "from math import pi" '
# i filen för att kunna använda pi..... men dete är bra övning om inget annat
# att behöva upptäcka det på egen hand. :)

radie = int(input("Skriv en radie av en cirkel så ska jag beräkna arean: "))
print(radie**2 * math.pi)

# Skriv ett program som tar höjden och basen på en triangel som input och utifrån det
# beräkna triangels area

basen = int(input("Ge mig basen av en triangel: "))
höjden = int(input("Ge mig höjden av en triangel: "))
area = basen * höjden / 2

print(area)

#Skriv ett program som löser ekvationen (x+y)*(x+y)

x = 5
y = 3

resultat = x * x + x * y + y * x + y * y 
print(resultat)

