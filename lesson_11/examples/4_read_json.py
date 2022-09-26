import json

with open("lesson_11/examples/data/persons.json") as f:
    cars = json.load(f)
    print(cars)
