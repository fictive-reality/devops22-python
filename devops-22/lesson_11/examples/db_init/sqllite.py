from db_init import open_connection, create_table, insert_data


def select_firstname_equals(connection, name):
    return tuple(connection.execute(
        '''
        SELECT
            firstname,
            lastname,
            timestamp
        FROM person
        WHERE
            firstname = ?
        ''', [name]
    ))


def select_firstname_like(connection, name):
    return tuple(connection.execute(
        '''
        SELECT
            firstname,
            lastname,
            timestamp
        FROM person
        WHERE
            firstname LIKE ?
        ''', [name]
    ))


def main():
    with open_connection("example.db") as conn:
        create_table(conn)
        insert_data(conn)
        print(select_firstname_like(conn, "C%"))
    conn.close()


if __name__ == "__main__":
    main()
