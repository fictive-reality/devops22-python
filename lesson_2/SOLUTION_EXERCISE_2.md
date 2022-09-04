# Exercise 2

## Instructions

The main goal of this exercise is to learn how to about python basics, to create variables, assign values, input & output, typing and operators.

### `Exercise` create a branch

If you want to save your work, you will need to create a branch.

1. Check with git status, it should output

    ```text
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

2. git branch `YOURUSERNAME_lesson_2`
3. git switch `YOURUSERNAME_lesson_2`
4. Check with git status, it should output

    ```text
    On branch YOURUSERNAME_lesson_2
    nothing to commit, working tree clean
    ```

### `Exercise` Printing

Create a program that `print` values

1. Print a integer value1

   ```python
    my_int = 4
    print(my_int)    
   ```

2. Print a float value

   ```python
    my_float = 4.0
    print(my_float)    
   ```

3. Print a String

   ```python
    my_string = "hello world"
    print(my_string)
   ```

4. Print a boolean value

   ```python
    my_bool = True
    print(my_bool)
   ```

5. Print a None value

   ```python
    my_nothing = None
    print(my_nothing)
   ```

6. Print a f-string containing all previous values in one line i.e 1, 1.0, "hello" ..

    ```python
    print(f'{my_int}, {my_float}, {my_string}, {my_bool}, {my_nothing}')
    ```

### `Exercise` Input

Create a program that uses `input` and type conversion

1. Input a string and assign it to a variable, then print the variable

    ```python
    name = input("write a name: ")
    print(name)
    ```

2. Input a number and assign it to a variable, print the value doubled

    ```python
    int_value = int(input("write integer value: "))
    print(int_value * 2)
    ```

3. Input a string i.e `hello` and assign it to a variable, print the string repeated `hellohello`

    ```python
    a_string = input("write some text: ")
    print(a_string * 2)
    ```

4. Input a float and assign it to a variable, print the value divided by 3.5

    ```python
    a_float = float(input("write a float: "))
    print(a_float / 3.5)
    ```
