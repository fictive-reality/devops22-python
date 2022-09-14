# Exercise Lesson 8

## Instructions

Todays exercises goal is to learn about exceptions and import

### `Exercise 1` raise

1. Create a function that check if a variable is a float, if not it raises a TypeError("message")

### `Exercise 2` input validation

1. Create a program that takes input and convert it to a integer
2. If it's not possible to convert it to a integer the program should print `Sorry, not an int`
3. If the input fail to convert to a int, the program should retry the input
4. If the number is even, raise a Exception('Even numbers is not allowed')

### `Exercise 3` try/except

1. Create a function that uses try/except
2. The function should have the parameters x, y
3. The function should return x/y
4. If the user provide a y = 0, it should except the error and print 'Division by zero is not allowed'
5. If the argument y is a string, it should raise a TypeError

### `Exercise 4` import

1. Import `sqrt` from `math`, calculate the sqrt of 16
2. Import `randint` from `random`, generate a random int 1 - 10
3. Import & Create a custom module
   1. Create a module named `calc.py`
   2. Add a function add that takes arguments x, y and return x + y.
   3. Import and use the function from `calc.py`

### `Exercise 5` lambda

1. Create a list with numbers from 1 - 10
2. Create a lambda expression that add 1 to each element: `lambda x: x + 1`
3. Apply the lambda on each element in the list with map(your_lambda, your_list)
4. Print a list from 3
