# Group Exercise Lesson 11

## Instructions

This is probably your first slightly larger program, so you will tackle it as a group exercise. Each team consists of 3-4 members. You can write your program fully object-oriented or not, this is up to your team to decide. The only requirement is that you somewhere use a class `Person`.

### `Exercise 1` Load data from a file

1. Create a file in either csv or json format (your choice). It should contain data for at least 5 Persons, you can create it manually or with a script.
2. A person has a firstname, lastname, birthdate and address.
3. Let the user enter the path to the file
4. Read the file and insert it into a SQLite database you have created.

### `Exercise 2` List all persons stored in the database

*Hint* here is a good place to use the class `Person`. e.g you can create a Person object for each row, and print it with a custom `__str__` method.

1. Create a (SQL) query that gets all rows (select *) from the table
2. Print all rows

### `Exercise 3` Menu

1. Create a menu with options:
   1. Load data from file (Use your solution from Exercise 1)
   2. List all persons (select *) (Use your solution from Exercise 2)
      1. EXTRA let the user type a firstname and query the database with that firstname
      2. EXTRA let the user type a lastname and query the database with that lastname
      3. EXTRA let the user type a birthdate and query query the database with that birthdate
      4. EXTRA let the user type an address and query the database with that address
   3. Delete a person
   4. EXTRA update a persons address with input from the user

### EXTRA EXTRA Add another table

Create another table, i.e Vehicles, Friends or Transactions. Make sure the content
would have some relation to Persons defined in the other table, e.g. a vehicle is owned
by a person or a transaction was done by a person.

1. Add it to your menu
2. Make it possible to add data to the second table
3. Query the database with a join between Person table and your second table, so you can see the combined results.
