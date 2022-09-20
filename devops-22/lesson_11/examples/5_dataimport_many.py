import json

with open("lesson_11/examples/data/persons.json") as f:
    data_to_database_executemany = []
    persons = json.load(f)
    for person in persons['persons']:
        data_to_database_executemany.append(tuple(person.values()))

print(data_to_database_executemany)
