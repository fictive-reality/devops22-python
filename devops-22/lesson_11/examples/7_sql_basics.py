import sqlite3

CREATE_TABLE_PERSON = '''
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                '''

INSERT_DATA = '''
            INSERT INTO person(
                firstname,
                lastname
            )
            VALUES (?, ?)
            '''

with sqlite3.connect('basic_example.db', isolation_level=None) as conn:
    conn.execute(CREATE_TABLE_PERSON)
    conn.execute(INSERT_DATA, ("Peter", "Svensson"))

conn.close()
