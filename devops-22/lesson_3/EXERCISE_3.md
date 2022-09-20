# Exercise 3

## Instructions

The goal of this exercise is to learn about Built-in Python Data Types, expressions, comparisons and strings

### `Exercise 1` create a branch

If you want to save your work, you will need to create a branch.

1. Check with git status, it should output

    ```text
    On branch main
    Your branch is up to date with 'origin/main'.

    nothing to commit, working tree clean
    ```

2. git branch `YOURUSERNAME_lesson_3`
3. git switch `YOURUSERNAME_lesson_3`
4. Check with git status, it should output

    ```text
    On branch YOURUSERNAME_lesson_3
    nothing to commit, working tree clean
    ```

### `Exercise 2` Data Types

see studentportalen `Datatyper_extra_övning.pdf`

### `Exercise 3` Boolean Operations - and, or, not

Create a program that creates three variables x, y, z as booleans. You can modify these variables to test your expressions.

```python
x = True
y = False
z = True
```

1. Write a expression with Boolean Operations that:
   1. result in True if any of x, y, z is True
   2. result in True if all x, y, z is True
   3. result in False if any of x, y, z is False
   4. result in False if all of x, y, z is False
   5. result in False if any of z, y, z is True
   6. result in False if all of z, y, z is True

### `Exercise 4` Data Structure - List

1. Create a empty list
2. Create a string that is a color e.g "red"
3. Add the color to your list
4. Print the color from the list using [Common Sequence Operations](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) indexing for `0` i.e my_list[0]
5. Add two other color to the list
6. Search for a color in the list using operation `x in s`
7. Verify that a color is not in the list using the operation `x not in s`
8. Create another list of colors and concatenate the two lists using the operation `s + t`
9. Create a list of two colors red, yellow with three of each color using the operation `s * n`
10. Print the first four colors in the list from (9) using the operation `s[i:j]`
11. Count how many times "red" occur in the list using the operation `s.count(x)`
12. Print the index of the first occurrence of "yellow" in s using the operation `s.index("yellow")`
13. Print the total length of each array using the operation `len(s)`
14. Create a list of 7 numbers
    1. Print the min value in the list
    2. Print the max value in the list

### `Exercise 5` Sorting

In LINKS_3.md there is a link Python guide how-to do [sorting](https://docs.python.org/3/howto/sorting.html). Create a list containing 10 car brand. i.e cars = ["volvo", ...]

1. Sort the list with `sorted(cars)`
2. Sort the list with `cars.sort()`
3. reverse the sort of both, read more about reversing in python docs [ascending-and-descending](https://docs.python.org/3/howto/sorting.html#ascending-and-descending)
4. *Extra* exercise, create a list of 10 tuples containing (brand, model), i.e ("volvo", "xc90"). Sort first on brand, then on model.
