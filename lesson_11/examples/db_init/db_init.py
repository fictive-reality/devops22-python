import sqlite3

EXAMPLE_DATASET = (
    (1, "Alice", "Smith"),
    (2, "Bob", "Smith"),
    (3, "Carol", "Brown"),
    (4, "Carlos", "Rojas"),
    (5, "Charlie", "Miller")
)

CREATE_TABLE = '''
                CREATE TABLE IF NOT EXISTS person(
                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    firstname TEXT,
                    lastname TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
                )
                '''

INSERT_DATA = '''
            INSERT INTO person(
                id,
                firstname,
                lastname
            )
            VALUES (?, ?, ?)
            '''


def open_connection(filename):
    return sqlite3.connect(filename, isolation_level=None)


def create_table(connection):
    try:
        connection.execute(CREATE_TABLE)
    except Exception:
        print('Failed to create table')
        raise


def insert_data(connection):
    try:
        with connection:
            connection.executemany(INSERT_DATA, EXAMPLE_DATASET)
    except sqlite3.IntegrityError:
        print("couldn't add Joe twice")
    except Exception:
        print("Failed to insert")
        raise
