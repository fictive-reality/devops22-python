import json

persons = {
    "persons": [{
        "firstname": "pelle",
        "lastname": "svensson",
        "year_of_birth": 1994
    },
        {
        "firstname": "olle",
            "lastname": "svensson",
            "year_of_birth": 1943
    },
        {
        "firstname": "nisse",
            "lastname": "svensson",
            "year_of_birth": 1967
    }
    ]

}

# https://docs.python.org/3/library/json.html
with open('lesson_11/examples/data/persons.json', 'w') as f:
    f.write(json.dumps(persons, indent=4))
