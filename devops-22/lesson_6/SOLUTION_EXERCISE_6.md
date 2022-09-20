# Exercise Lesson 6

## Instructions

Todays exercises goal is to learn more about collections, we will work with the `stack`, `queue` and `Counter`.

### `Exercise 1` Dataset

Todays exercises requires that you generate test data. You can generate data in multiple ways i.e manually through loops, using `random` module or list comprehension. See examples in `8_data.py`.

1. Generate a list containing the numbers 1, 2, 3 to 100.

    ```Python
    list(range(1, 101))
    ```

2. Generate a list of all even numbers from 2 to 60

    ```Python
    list(range(2, 61, 2))
    ```

3. Generate a list of all odd numbers from 1 to 77

    ```Python
    list(range(1, 78, 2))
    ```

4. Generate a list of 100 numbers between 1 - 300
    1. The numbers must be unique

        ```Python
        from random import sample
        population = list(range(1, 301))
        hundred_numbers = sample(population, k=100)
        ```

    2. The numbers are selected randomly (not unique)

        ```Python
        from random import choices
        population = list(range(1, 301))
        hundred_numbers = choices(population, k=100)
        ```

5. create a list containing five colors (not containing red)
   1. Create a new list containing "red" and also add two colors by random with `choice`, `choices` or `sample` from the list.

        ```Python
        from random import sample
        colors = ["yellow", "blue", "green", "black", "white"]
        new_list = ["red"]
        new_list.extend(sample(colors, k=2))
        ```

   2. Generate a list of random colors from the list of 3, the list should be of length 50.

        ```Python
        from random import sample, choice
        # Part 1
        colors = ["yellow", "blue", "green", "black", "white"]
        new_list = ["red"]
        new_list.extend(sample(colors, k=2))

        # Part 2
        random_colors = choices(new_list, k=50)
        ```

   3. Print the length of all three lists and the unique colors in each list

        ```Python
        # Code from above
        unique_colors = set(colors)
        colors_string = ", ".join()
        print(f'{len(colors)} {colors_string}')
        print(f'{len(new_list)} {", ".join(set(new_list))}')
        print(f'{len(random_colors)} {", ".join(set(random_colors))}')
        ```

<div class="page"/>

### `Exercise 2` Name Counter

1. Generate a list with 100 elements, i.e ["johan", "lisa", "johan", "tove"...]
2. Count the names i.e ('lisa', 1), ('johan',2)
3. Print the top 3 most popular names
4. Print the least popular name[s]
5. Print all unique names
   1. In alphabetical order
   2. Shuffled
   3. In reversed alphabetical order

Solution:

```Python
# Step 1
from random import choices

names = choices(["johan", "lisa", "johan", "tove"], k=100)

# Step 2
from collections import Counter
names_counter = Counter(names)

# Step 3
print(names_counter.most_common(3))

# Step 4
print(names_counter.most_common()[-1])

# Step 5

#  1. In alphabetical order
unique_names = sorted(list(set(names)))
print(unique_names)

#  2. Shuffled
from random import shuffle
shuffle(unique_names)
print(unique_names)

#  3. In reversed alphabetical order
unique_names.sort(reverse=True)
print(unique_names)
```

<div class="page"/>

### `Exercise 3` Stack

1. Generate a list of lowercase a-z
2. Iterate through the alphabet and append each letter to a stack
3. Pop all elements and print on one line as a string

```Python
# Part 1
import string

list(string.ascii_lowercase)

# Part 2
my_stack = []
for letter in string.ascii_lowercase:
    my_stack.append(letter)

# Part 3
my_string = ""
while my_stack:
    my_string += my_stack.pop()

print(my_string)
```

<div class="page"/>

### `Exercise 4` Queue

Use the deque FIFO, first in, first out. I.e if ["lisa", "olle", "pelle"] is in the list, then use pop left so that "lisa" is first to leave the queue.

1. Generate a list with 50 names
2. Create a Queue `deque` with a maximum length of 10
3. Let random number of person leave the queue
4. When the random number of persons has left the queue, fill the missing spots
5. Iterate until all 50 has gone through the queue

Solution

```Python
from collections import deque
from random import randint
names = ["pelle", "lisa", "olle", "tove", "petter"] * 10

queue = deque(maxlen=10)


while len(names):
    random_number = randint(0, 10)
    for i in range(random_number):
        if len(queue):
            print(queue.popleft())

    for i in range(random_number):
        if len(names):
            queue.append(names.pop())
```

<div class="page"/>

### `Exercise 5` Named tuple

1. Create a named tuple with the coordinates (x, y)
2. Create two points
3. Print the points in a board i.e

    ```Python
    # Generate a board
    board = [["-"]*10 for i in range(10)]

    # mark x, y in board as *
    board[1][2] = '*'
    board[4][6] = '*'

    # Print board
    for row in board:
        print(row)
    ```

4. Calculate the Euclidean distance (hypotenuse) for Point1 and Point2, i.e (1, 2) and (4, 6) has the distance 5.

Solution:

```Python
from collections import namedtuple

Coords = namedtuple('Coordinates', ['x', 'y'])

point_1 = Coords(1, 1)
point_2 = Coords(4, 5)

# Generate a board
board = [["-"]*10 for i in range(10)]

# mark x, y in board as *
board[point_1.x][point_1.y] = '*'
board[point_2.x][point_2.y] = '*'


# Print board
for row in board:
    pass
    print(row)

x_distance = point_2.x - point_1.x
y_distance = point_2.y - point_1.y

print((x_distance**2 + y_distance**2) ** 0.5)
```

<div class="page"/>

### `Exercise 6` Copy

1. Create string variable
2. Create second variable and assign the first variable to it
3. Create a third variable and assign a copy of the first variable
4. Change the second variable
5. Print all variables, what differs?

```Python
# Part 1
my_string = "hello"

# Part 2
my_other_string = my_string

# Part 3
my_third_string = my_string[:]

# Part 4
my_other_string = "Howdy"  # String is immutable, so this is a re-assignment not a change

# Part 5

print(my_string)
print(my_other_string)
print(my_third_string)

# String is immutable.

```

<div class="page"/>

### `Exercise 7` Deep copy

1. Create a list with names
2. Assign the list to a variable
3. Create a copy and a deep copy
4. pop one element in the original list and append a new name
5. Print all lists, what differs?

```Python
# Step 1 & 2
names = ["list", "pelle", "olle", "tove"]

# Step 3
from copy import copy, deepcopy

names_copy = copy(names)
names_deep_copy = deepcopy(names)

# Step 4
names.pop()
names.append("Tor")

print(names)
print(names_copy)
print(names_deep_copy)
```
