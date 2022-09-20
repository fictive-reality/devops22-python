import json

with open("lesson_11/examples/data/persons.json") as f:
    persons = json.load(f)
    for person in persons['persons']:
        # Use this in executes second argument
        executeValues = tuple(person.values())
        print(executeValues)
