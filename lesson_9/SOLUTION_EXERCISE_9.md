# Exercise Lesson 9

## Instructions

### `Exercise 1` class

1. Create classes
   1. Create a class Animal
   2. Create a class Dog
   3. Create a class Supermarket
   4. Create a class Coop
2. Use Animal as a base class for Dog

Solution

```Python
# 1.
class Animal:
    pass


class Dog:
    pass


class Supermarket:
    pass


class Coop:
    pass


# 2.

class Dog(Animal):
    pass
```

<div class="page"/>

### `Exercise 2` `__init__`

In your class create a `__init__`function, i.e

```Python
class MyClass:
    
    def __init__(self, my_arg):
        self.my_arg = my_arg

```

1. Create a class Animal with a `__init__` that takes 1 argument
2. Create a class Dog with a `__init__` that takes 2 arguments
3. Create a class Supermarket with a `__init__` that takes 3 arguments
4. Create a class Coop with a `__init__` that takes 4 arguments

    ```Python
    # To test your code, you can create a main

    class MyCLass:
        pass


    if __name__ == '__main__':
        my_class = MyClass("my_string")
    ```

Solution

```Python

# 1
class Animal:

    def __init__(self, family):
        self.family = family


# 2
class Dog:

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


# 3
class Supermarket:

    def __init__(self, location, store_open, store_close):
        self.location = location
        self.store_open = store_open
        self.store_close = store_close


# 4
class Coop:

    def __init__(self, location, store_open, store_close, store_type):
        self.location = location
        self.store_open = store_open
        self.store_close = store_close
        self.store_type = store_type
```

<div class="page"/>

### `Exercise 3` methods

```Python

class MyClass:
    
    def __init__(self, my_arg):
        self.my_arg = my_arg

    def my_method(self):
        return self.my_arg * 2
```

1. Create a class Square:
   1. The Square takes 1 argument `side`
   2. The Square should have a method `area`
      1. Area is calculated by side ** 2
      2. Area should be returned as a float
   3. The Square should have a method `circumference`
      1. Circumference is calculated by side * 4
      2. Circumference should be returned as a float
2. Instantiate a object for
   1. a square with side 2 and calculate the area & circumference
   2. a square with side 3.5 and calculate the area & circumference

Solution

```Python
class Square:

    def __init__(self, side):
        self.side = side

    def area(self):
        return float(self.side ** 2)

    def circumference(self):
        return 4.0 * self.side


def main():
    square_one = Square(2)
    print(square_one.area())
    print(square_one.circumference())

    square_two = Square(3.5)
    print(square_two.area())
    print(square_two.circumference())


if __name__ == '__main__':
    main()
```

```Python
# Example how to instantiate and call methods

class MyClass:
    # Your code

if __name__ == '__main__':
    my_object = MyClass("args")
    print(my_class.my_method())    

    my_another_object = MyClass("args")
    print(my_another_object.my_method())  
```

<div class="page"/>

### `Exercise 4` Circle

1. Create a class Circle
   1. Provide the diagonal as a argument
   2. Import pi from math.pi
   3. Calculate the area in a method
   4. Calculate the circumference in a method
   5. Use your created methods to calculate the area and circumference directly in `__init__`
   6. Add a color variable, the default color should be `grey` for all objects
   7. Add a method that can set a variable color on the circle i.e `my_circle.set_color("red")`

```Python
# Call a method from your __init__

class MyClass:
    
    def __init__(self):
        self.a_variable = 'a value'
        self.do_something()
        

    def do_something(self):
        pass
        # code..

if __name__ == '__main__':
    my_class = MyClass()

    # To print the variable
    print(my_class.a_variable)
```

Solution

```Python
from math import pi


class Circle:

    def __init__(self, diagonal):
        self.diagonal = diagonal
        self.color = 'grey'
        self.area = self.calc_area()
        self.circumference = self.calc_circumference()

    def calc_area(self):
        return pi * (self.diagonal / 2) ** 2

    def calc_circumference(self):
        return self.diagonal * pi

    def set_color(self, color):
        self.color = color


def main():
    circle = Circle(2)
    print(circle.area)
    print(circle.circumference)
    print(circle.color)
    circle.set_color("red")
    print(circle.color)


if __name__ == '__main__':
    main()

```

<div class="page"/>

### `Exercise 5` EXTRA - Base class

```Python
# Minimal base class example

class Animal:
    pass

class Dog(Animal):
    pass
```

1. Create a class `Person`
    1. A person has a name
    2. A person has a year of birth
2. Create a class `Player` that uses `Person` as a base
    1. A player has speed 1-10
    2. A player has agility 1-10
    3. A player has strength 1-10
3. Create a class `Coach` that uses `Person` as a base
   1. A couch has a voice_level 1-10
4. Create a class `Team`
   1. A team has players in a list
   2. A team has a coach
   3. Write a method that can summarize the team composition.

```Python
# Tips you can use __str__ to easily print a object

class MyClass:

    def __str__(self):
        return f"{self.name} - other text"

if __name__ == '__main__':
    my_class = MyClass()

    # To print the object
    print(my_class)
```

Solution

```Python
import random


class Person:

    def __init__(self, name, year):
        self.name = name
        self.year = year


class Player(Person):

    def __init__(self, name, year, stats):
        super().__init__(name, year)
        self.stats = stats

    def __str__(self):
        return f"{self.name} [{self.year}] - {self.stats}"


class Coach(Person):

    def __init__(self, name, year, voice):
        super().__init__(name, year)
        self.voice = voice

    def __str__(self):
        return self.name


class Team:

    def __init__(self, players, coach):
        self.players = players
        self.coach = coach

    def summarize_team(self):
        team = """
-------------------------------------
-------------- My team --------------
-------------------------------------
"""
        team += f"Coach {self.coach}\n"
        team += "-------------- Players --------------\n"
        team += "\n".join(map(str, self.players))
        return team


def get_random_stats():
    return (
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10))


def main():
    coach = Coach("Pelle", 1959, 5)

    players = []
    for name in ["lisa", "eva", "petra", "linda", "amanda", "jonna", "malin", "fredrika", "frida", "jenny"]:
        year = random.randint(1987, 2004)
        players.append(Player(name, year, get_random_stats()))

    team = Team(players, coach)
    print(team.summarize_team())


if __name__ == '__main__':
    main()
```
