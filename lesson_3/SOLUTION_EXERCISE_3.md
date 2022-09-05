# Exercise 3

## Instructions

The goal of this exercise is to learn about Built-in Python Data Types, expressions, comparisons and strings

### `Exercise 1` create a branch

If you want to save your work, you will need to create a branch.

### `Exercise 2` Data Types

see studentportalen `Datatyper_extra_övning.pdf`

### `Exercise 3` Boolean Operations - and, or, not

```python
x = True
y = False
z = True
```

Write a expression with Boolean Operations that:
   1. result in True if any of x, y, z is True

```python
(x or y or z)
```

   2. result in True if all x, y, z is True

```python
(x and y and z)
```

   3. result in False if any of x, y, z is False

```python
(x and y and z)
```

   4. result in False if all of x, y, z is False

```python
(x or y or z)
```

   5. result in False if any of z, y, z is True

```python
(not (x or y or z))
```

   6. result in False if all of z, y, z is True

```python
(not (x and y and z))
```

### `Exercise 5` Sorting

In LINKS_3.md there is a link Python guide how-to do [sorting](https://docs.python.org/3/howto/sorting.html). Create a list containing 10 car brand. i.e cars = ["volvo", ...]

```python
cars = ["volvo", "saab", "audi", "skoda", "volkswagen", "tesla", "kia", "toyota", "lexus", "bmw"]
```

1. Sort the list with `sorted(cars)`

    ```python
    sorted_cars = sorted(cars)
    print(sorted_cars)
    ```

2. Sort the list with `cars.sort()`

    ```python
    cars.sort()
    print(cars)
    ```

3. reverse the sort of both, read more about reversing in python docs [ascending-and-descending](https://docs.python.org/3/howto/sorting.html#ascending-and-descending)

    ```python
    sorted_cars = sorted(cars, reverse=True)
    print(sorted_cars)

    cars.sort(reverse=True)
    print(cars)
    ```

4. *Extra* exercise, create a list of 10 tuples containing (brand, model), i.e ("volvo", "xc90"). Sort first on brand, then on model.

    ```python
    # https://docs.python.org/3/howto/sorting.html#operator-module-functions
    cars = [("volvo", "xc90"),  ("saab", "900"), ("audi", "r8"), ("skoda", "yeti"), ("volkswagen","passat"), ("tesla", "model s"), ("kia", "niro"), ("toyota", "rav4"), ("lexus", "rx 350"), ("bmw", "m3")]
    cars.sort()
    print(cars)

    # Custom order is possible with itemgetter, but this is not needed in this case
    # from operator import itemgetter
    # sorted(cars, key=itemgetter(0,1))

    ```
