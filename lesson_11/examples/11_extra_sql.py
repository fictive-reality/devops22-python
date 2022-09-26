import sqlite3
from tabulate import tabulate

try:
    with sqlite3.connect(':memory:', isolation_level=None) as conn:
        conn.execute(
            """
            CREATE TABLE customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                firstname TEXT,
                lastname TEXT
            )
            """)

        conn.execute(
            """
            CREATE TABLE orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                customer_id INTEGER NOT NULL,
                status TEXT
            )
            """)

        conn.executemany(
            """
            INSERT INTO customers (
                firstname,
                lastname
            ) VALUES(?, ?)
            """, (("Nils", "Smith"), ("Adam", "Williams"), ("Joe", "Clinton")))

        conn.executemany(
            """
            INSERT INTO orders (
                customer_id,
                status
            ) VALUES(?, ?)
            """, ((1, "shipped"), (1, "prepared"), (2, "cancelled")))

        customer_orders = conn.execute(
            """
            SELECT o.id as order_id, c.id as customer_id, c.firstname, c.lastname, o.status
            FROM orders AS o
            INNER JOIN customers AS c ON o.customer_id=c.id
            """
        )

        description = tuple(map(lambda x: x[0], customer_orders.description))
        print(tabulate(customer_orders.fetchall(), description))

except Exception as e:
    print(e)
finally:
    conn.close()
