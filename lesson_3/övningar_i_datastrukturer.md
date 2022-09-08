Övningar i datastrukturer
Uppgift A
Skapa ett nytt python-dokument i din utvecklingsmiljö, glöm inte ändelsen .py. Skriv av
nedanstående program och laborera fram svaret på frågorna nedan. Det är alltså fritt fram
att lägga till nya rader i programmet. Var noga när du skriver av så att till exempel ett ”{“ inte
byts ut mot ett “[“. Det är viktigt att du förstår vad som händer och varför. Tips: Kommandot
type(X) returnerar X:s datatyp.

X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5",
"Bella": "Klockgatan 1",
"Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

Frågor:
1. Vilken datatyp har variablerna X och Y?
   Svar: Integer

2. Vilken datatyp har variabeln addresses?
   Svar: Dictionaries 

3. Hur kan man få ut bellas adress ur variabeln addresses?
   Svar: print(addresses["Bella"]) hämtar bellas adress ur dict.
4. Vad händer om man skriver addresses[“Daniel”] = “Prinsgränd 2”?
   Svar: Man lägger till Daniel och adress i "addresses". (dict.)
5. Få ditt program att skriva ut hur många keys addresses har.
   Svar: "print(len(addresses))"

5.1. Utöka programmet så att adressen skrivs ut till den personen som
kommer sist i bokstavsordning.
    Svar: print(list(addresses)[-1])

5.2. Utöka programmet så att namnet skrivs ut på den personen som bor
på adressen som kommer först i bokstavsordning. Tips: följande rad
byter plats på keys och values i my_dict:
my_dict = {v: k for k, v in my_dict.items()}
Förklaring kommer nästa lektion!
   Svar: addresses = {v: k for k, v in addresses.items()}  -  print(f'{list(addresses)[-1]}')
      
6. Vilken datatyp har variabeln cars?
   Svar: List

7. Vad returneras om man skriver cars[X]?
   Svar: Opel

8. Vad returneras om man skriver cars[Y], varför?
   Svar: IndexError: list index out of range. Listan som man försöker printa är inte så lång som värdet på "Y" har.

9. Vad returneras om man först skriver cars.sort() och på nästa rad skriver
cars[0]?
    Svar:BMW.

10. Skapa en ny variabel genom att skriva cars_2 = cars, och på följande rad ska
strängen “Saab” läggas till cars med hjälp av append(). Notera att det alltså
bara är ena variabeln som ska utökas. Vad innehåller variablerna cars_2 och
cars nu? Förklara!
    Svar: cars_2 kopierar cars innan saab läggs till. Så cars innehåller saab men inte cars_2.

10.1. Skapa ytterligare en variabel cars_3 som får sina element av cars
men som inte påverkas av vad som läggs till i cars.
    Svar: cars_3 = cars_2.copy()

10.2. Utöka variabeln cars så att den innehåller dubbletter av varje bilmärke
sorterat i omvänd bokstavsordning.
   Svar: cars.sort(reverse = True)

10.3. Från den utökade versionen av cars ifrån förra uppgiften, skapa
variabeln unique_cars som ska vara en lista där varje bilmärke finns
med exakt en gång.
Svar: --

1.  Vilken datatyp har variablerna numbers1 och numbers2?
      Svar: Set

2.  Vilka värden finns lagrade i variablerna numbers1 och numbers2?
      Svar: Int samt constant med sparade int's.

3.  Vad är snittet (intersection) mellan variablerna numbers1 och numbers2?
      Svar: Intersectionen mellan numbers_1 och numbers_2 är 2 & 3. Snittet är således 2,5.

4.  Vad är unionen mellan variablerna numbers1 och numbers2?
      Svar: {1, 2, 3, 4, 6, 7}
5.  Vilken är den symmetriska differensen mellan numbers1 och numbers2?
      Svar: {1, 6}

Uppgift B
Projektledaren för ditt utvecklingsteam kommer till dig och vill att du ska skriva ett program.
Programmet har en kravspecifikation enligt punkterna 1-4 nedan. Projektledaren kan inte
programmera så för att hen ska kunna läsa din kod ber hen dig att undvika att använda
loopar och if-satser, om du kan.
1. Programmet ska vara icke-case-sensitive. Det ska alltså inte spela någon roll
om användaren använder stora eller små bokstäver. Namn som skrivs ut ska
dock alltid börja med stor bokstav.
2. Programmet ska låta användaren mata in tre personers namn, ålder och
skostorlek. Dessa uppgifter måste sparas under programmets körning.
3. Programmet ska sedan skriva ut namn och skostorlek på den person som är
äldst samt namn och ålder på den som har medianskostorlek.
4. Efter det ska användaren kunna söka efter personer genom att mata in en av
de tre datatyperna. Om programmet hittar någon som matchar ska dennes
kompletta uppgifter skrivas ut.
Du är fri att designa ditt program hur du vill inom ramen för specifikationen men en
exempelkörning kan se ut som följer:
Please enter name for person 1
>ahmed
Please enter age for person 1
>25
Please enter shoe size for person 1
>42
Please enter name for person 2
>DIANA
Please enter age for person 2
>40
Please enter shoe size for person 2
>38
Please enter name for person 3
>Casper
Please enter age for person 3
>30
Please enter shoe size for person 3
>45
The oldest person is Diana who has shoe size 38
The person with median shoe size is Ahmed who is 25 years old
Please enter search value, name, age or size followed by value
>age 30
Found person
Name: Casper
Age: 30
Size: 45