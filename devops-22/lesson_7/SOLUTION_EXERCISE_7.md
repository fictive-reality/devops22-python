# Exercise Lesson 7

## Instructions

Todays exercises goal is to learn about basic functions.

### `Exercise 1` Functions

1. Create a function with name `do_nothing`
   1. The function should have a `pass`
   2. Call the function from your code

   ```Python
   def do_nothing():
      pass

   do_nothing() 
   ```

2. Functions getting started:
   1. Create a function that prints `hello world`
   2. Create a function that prints the result from `1 == 1.0`
   3. Create a function that prints the alphabet in reverse order
   4. Assign the previous 1-3 to variables, and print the value. It should return `None`

   ```Python
   
   def hello():
      print("hello world")
   
   def ones():
      print(1 == 1.0)

   import string
   def rev_alpha():
      print(string.ascii_lowercase[::-1])

   var_1 = hello()
   var_2 = ones()
   var_3 = rev_alpha()

   print(f"{var_1} {var_2} {var_3}")

   ```

3. Functions with arguments
   1. Create a function that prints `hello name` with name as a parameter
   2. Create a function that prints a string in capital letters, with `word` as a parameter
   3. Create a function that prints numbers between 1 and `stop`, where stop is a parameter

   ```Python
   def hello(name):
      print(f"hello {name}")

   def cap(word):
      print(word.upper())

   def number_printer(stop):
      print(list(range(1, stop)))

   ```

### `Exercise 2` Default Arguments

1. Create a function that prints 1 to 10 by default, i.e `start=1` `stop=11` and uses a range in the function block.
2. Create a function that by default prints a string, if `reverse=True` is used as argument the string is printed in reverse.
3. Call the same function with and without reverse

   ```Python
   def default_number_printer(start=1, stop=11):
      print(list(range(start, stop)))

   def rev_string(word, reverse=False):
      if reverse:
         word = word[::-1]
      print(word)

   rev_string("hello")
   rev_string("hello", reverse=True)

   ```

### `Exercise 3` Return

1. Create a function that returns a integer
2. Create a function that returns a tuple with (x, y) value
3. Create a function that returns a boolean value
4. Create a function that returns a float
5. Create a function that has `firstname` and `lastname` as parameters and returns fullname.
6. Create a function that calculates the area of a rectangle and returns the result
7. Create a function that has a list as parameter, the list should contain of values and the function returns the sum of all elements in the list.
8. Create a function that repeats a word multiple time, `word` and `repeat` is used as parameters. If the word is hello and repeat is 3, it will print hello three times.

   ```Python

   def get_number():
      return 1
   
   def get_tup(x, y):
      return x, y

   def get_bool():
      return True

   def get_float():
      return 1.0

   def fullname(firstname, lastname):
      return f'{firstname} {lastname}'

   def area(l, b):
      return l*b

   def sum_list(values):
      return sum(values)

   def echo(word, repeat):
      for r in range(repeat):
         print(word)

   echo("hello", 3)

   ```
