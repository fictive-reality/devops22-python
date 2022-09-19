import sqlite3

# A memory database can be used when learning. A new one will be created every run.
connection = sqlite3.connect(":memory:", isolation_level=None)

connection.execute("""
                CREATE TABLE person(
                id INTEGER PRIMARY KEY,
                firstname,
                lastname
              )""")

connection.execute("""INSERT INTO person(
                id,
                firstname,
                lastname
                ) VALUES (
                    1,
                    'john',
                    'smith'
                )""")

connection.execute("""INSERT INTO person(
                id,
                firstname,
                lastname
                ) VALUES (
                    2,
                    'admin',
                    'smith'
                )""")


for person in connection.execute("SELECT * FROM person"):
    print(person)

connection.close()
