# Exercise Lesson 6

## Instructions

Todays exercises goal is to learn more about collections, we will work with the `stack`, `queue` and `Counter`.

### `Exercise 1` Dataset

Todays exercises requires that you generate test data. You can generate data in multiple ways i.e manually through loops, using `random` module or list comprehension. See examples in `8_data.py`.

1. Generate a list containing the numbers 1, 2, 3 to 100.
2. Generate a list of all even numbers from 2 to 60
3. Generate a list of all odd numbers from 1 to 77
4. Generate a list of 100 numbers between 1 - 300
    1. The numbers must be unique
    2. The numbers are selected randomly (not unique)
5. create a list containing five colors (not containing red)
   1. Create a new list containing "red" and also add two colors by random with `choice`, `choices` or `sample` from the list.
   2. Generate a list of random colors from the list of 3, the list should be of length 50.
   3. Print the length of all three lists and the unique colors in each list

### `Exercise 2` Name Counter

1. Generate a list with 100 elements, i.e ["johan", "lisa", "johan", "tove"...]
2. Count the names i.e ('lisa', 1), ('johan',2)
3. Print the top 3 most popular names
4. Print the least popular name[s]
5. Print all unique names
   1. In alphabetical order
   2. Shuffled
   3. In reversed alphabetical order

### `Exercise 3` Stack

1. Generate a list of lowercase a-z
2. Iterate through the alphabet and append each letter to a stack
3. Pop all elements and print on one line as a string

<div class="page"/>

### `Exercise 4` Queue

Use the deque FIFO, first in, first out. I.e if ["lisa", "olle", "pelle"] is in the list, then use pop left so that "lisa" is first to leave the queue.

1. Generate a list with 50 names
2. Create a Queue `deque` with a maximum length of 10
3. Let random number of person leave the queue
4. When the random number of persons has left the queue, fill the missing spots
5. Iterate until all 50 has gone through the queue

### `Exercise 5` Named tuple

1. Create a named tuple with the coordinates (x, y)
2. Create two points
3. Print the points in a board i.e

    ```Python
    # Generate a board
    board = [["-"]*10 for i in range(10)]

    # Print board
    for row in board:
        print(row)

    # mark x, y in board as *
    board[1][2] = '*'
    board[4][6] = '*'
    ```

4. Calculate the Euclidean distance (hypotenuse) for Point1 and Point2, i.e (1, 2) and (4, 6) has the distance 5.

### `Exercise 6` Copy

1. Create variable with a string
2. Create second variable and assign the first variable to it
3. Create a third variable and assign a copy of the first variable
4. Change the second variable
5. Print all variables, what differs?

### `Exercise 7` Deep copy

1. Create a list with names
2. Assign the list to a variable
3. Create a copy and a deep copy
4. pop one element in the original list and append a new name
5. Print all lists, what differs?
