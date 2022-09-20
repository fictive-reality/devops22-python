import csv

with open("lesson_11/examples/data/cars.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
