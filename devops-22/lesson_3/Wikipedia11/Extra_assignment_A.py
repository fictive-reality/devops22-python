Uppgift A

Skapa ett nytt python-dokument i din utvecklingsmiljö, glöm inte ändelsen .py. Skriv av
nedanstående program och laborera fram svaret på frågorna nedan. Det är alltså fritt fram
att lägga till nya rader i programmet. Var noga när du skriver av så att till exempel ett ”{“ inte
byts ut mot ett “[“. Det är viktigt att du förstår vad som händer och varför. 

Tips: Kommandot type(X) returnerar X:s datatyp.

X = 1
Y = 4

addresses = {"Adam": "Ormvägen 5", "Bella": "Klockgatan 1", "Cornelia": "Vikingagatan 3"}

cars = ["Volvo", "Opel", "BMW"]

numbers1 = {1, 2, 3, X, 6}

numbers2 = {Y, 2, 3, 4, 7}

Frågor:

1. Vilken datatyp har variablerna X och Y?

2. Vilken datatyp har variabeln addresses?

3. Hur kan man få ut bellas adress ur variabeln addresses?

4. Vad händer om man skriver addresses[“Daniel”] = “Prinsgränd 2”?

5. Få ditt program att skriva ut hur många keys addresses har.

5.1. Utöka programmet så att adressen skrivs ut till den personen som
kommer sist i bokstavsordning.

5.2. Utöka programmet så att namnet skrivs ut på den personen som bor
på adressen som kommer först i bokstavsordning. Tips: följande rad
byter plats på keys och values i my_dict:
my_dict = {v: k for k, v in my_dict.items()}
Förklaring kommer nästa lektion!

6. Vilken datatyp har variabeln cars?

7. Vad returneras om man skriver cars[X]?

8. Vad returneras om man skriver cars[Y], varför?

9. Vad returneras om man först skriver cars.sort() och på nästa rad skriver
cars[0]?

10. Skapa en ny variabel genom att skriva cars_2 = cars, och på följande rad ska
strängen “Saab” läggas till cars med hjälp av append(). Notera att det alltså
bara är ena variabeln som ska utökas. Vad innehåller variablerna cars_2 och
cars nu? Förklara!

10.1. Skapa ytterligare en variabel cars_3 som får sina element av cars
men som inte påverkas av vad som läggs till i cars.

10.2. Utöka variabeln cars så att den innehåller dubbletter av varje bilmärke
sorterat i omvänd bokstavsordning.

10.3. Från den utökade versionen av cars ifrån förra uppgiften, skapa
variabeln unique_cars som ska vara en lista där varje bilmärke finns
med exakt en gång.

11. Vilken datatyp har variablerna numbers1 och numbers2?

12. Vilka värden finns lagrade i variablerna numbers1 och numbers2?

13. Vad är snittet (intersection) mellan variablerna numbers1 och numbers2?

14. Vad är unionen mellan variablerna numbers1 och numbers2?

15. Vilken är den symmetriska differensen mellan numbers1 och numbers2?