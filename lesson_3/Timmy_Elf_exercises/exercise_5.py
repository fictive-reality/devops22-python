#Sorting

car = ["Tesla", "Ferrari", "BMW", "Ford", "Volvo", "Mercedes", "Skoda", "Audi", "JEEP", "SAAB"]

#1. 
print(sorted(car))

#2. 
car.sort()

print(car)

#3. 
print(sorted(car, reverse = True))

car.sort(reverse = True)

print(car)

#4. 
car_3 = [
    ("Tesla",    "1"),
    ("Ferrari",  "2"), 
    ("BMW",      "3"),
    ("Ford",     "4"),
    ("Volvo",    "5"),
    ("Mercedes", "6"),
    ("Skoda",    "7"),
    ("Audi",     "8"),
    ("JEEP",     "9"),
    ("SAAB",     "10")
    ]

car_3.sort()
print(car_3)