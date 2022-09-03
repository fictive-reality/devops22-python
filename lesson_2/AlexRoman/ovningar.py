# Övningar föreläsning 2
"""
1. Om man skriver 
A=5
B=A
A=7
C = A+B
Vad blir då värdet på C? Vad trodde du att det skulle bli?
"""
A = 5
B = A
A = 7
C = A + B
print(C)


"""
2. Om man skriver A = 7 * 3 +1
Vad blir värdet på A?
"""
A = 7*3+1
print(A)


"""
3. Om
A = 20/4*2
Vad blir A? Vad kan man göra för att slippa missförstånd kring vad A blir?
"""
A = 20/4*2
print(A)


"""
4. Om 
A=1
B=A
A=A+B
B=A+B
C=A+B
Vad blir värdet på C?
"""
A=1
B=A
A=A+B
B=A+B
C=A+B
print(C)


"""
5. Använd python för att skriva “Hello World” till skärmen
"""
print("Hello World")


"""
6. Skriv ett program som först ber användaren om tal A, sedan tal B
a. Skriv ut summan av de båda talen
b. Skriv ut skillnaden mellan de båda talen
c. Skriv ut de båda talen multiplicerade med varandra.
"""
number1 = input("Type a number: ")
number2 = input("Type another number: ")

sum = int(number1) + int(number2)
dif = int(number1) - int(number2)
mult = int(number1) * int(number2)

print("The sum is: ", sum)
print("The difference is: ", dif)
print("First number multiplied by the second number is: ", mult)


"""
7. Ta in två tal från användaren som i uppgiften ovan och
a. Använd division för att se vad de olika talen blir delat på varandra
b. Samma som 3.a, men använd heltalsdivision, skriv resultatet till skärm.
"""
div_ab = int(number1) / int(number2)
div_ba = int(number2) / int(number1)
print(f"First number divided by the second number is:  {div_ab} or {int(div_ab)} (heltal)")
print(f"Second number diveded by the first number is:  {div_ba} or {int(div_ba)} (heltal)")


"""
8. Skriv ett program som tar in radien på en cirkel från användaren och beräknar cirkelns area
 Vägledning: Ni måste skriva ​from math import pi​ i ert program för att 
 kunna använda ett mycket exakt pi i beräkningarna. 
 Om ni inte bryr er om att vara exakta går det bra att bara sätta pi till 3,14
"""



"""
9. Skriv ett program som tar höjden och basen på en triangel som input, och utifrån det beräknar triangels area
"""




"""
10. Skriv ett program som löser ekvationen (x+y)*(x+y)
"""




"""
11. Skriv ett program som räknar ut hypotenusan I en rätsidig triangel
Vägledning: Ni behöver skriva in​ from math import sqrt i​ källkodsfilen
"""



"""
12. Skriv ett program som räknar ut antalet timmar och minuter det går på 455 minuter.
"""



"""
13. Skriv ett program som ber användaren att skriva in ett antal sekunder och sedan 
räknar ut hur många dagar, timmar, minuter och sekunder det går på de sekunderna.
"""



"""
14. a = okänt variabel b = okänt variabel. (Vilka som helst, integer, float eller 
string som du sätter själv) a få samma värde som b och b samma som a :
a. Skriv koden som gör det som står på raden ovan. Använd gärna hjälp variabel “c” för att klara uppgiften.
b. Skriv koden som gör det utan att använda någon hjälpvariabel.
"""



"""
15. Använd multipel tilldelning för att ge x, y, z samma värde
"""



"""
16. Be användaren att skriva in olika temperaturer, konvertera sedan temperaturen till 
fahrenheit Fahrenheit = Celsius * 9/5 + 32
Formula
"""



"""
17. Skapa ett program som frågar användaren efter deras namn och ålder.
 Programmet ska sedan skriva ut vilket år användaren fyller 100 och vilket år användaren föddes.
"""



"""
18. Skapa ett program som frågar användaren efter ett nummer. Beroende på om siffran är udda 
eller jämnt ska programmet skriva ut olika meddelanden. 
​Tips: I denna uppgift behöver du en så kallad if-sats. Använd google för att förstå hur en if-sats fungerar​.
"""



"""
19. Din kollega har skickat ett litet program till dig enligt nedan. 
Det fungerar visserligen, men vad har du för kommentarer till din kollegas programmeringsstil?
print​(​"Detta är mitt bästa program"​) ​# Här skriver jag ut en liten välkomsthälsning till 
användaren av detta program
A = ​int​(​input​())
Ålder = ​int​(A) ​# Skriv till fönster
#minInputVariabel = float(A)
print​(​"Ålder"​, A)
"""