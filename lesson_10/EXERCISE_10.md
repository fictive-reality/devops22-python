# Exercise Lesson 10

## Instructions

Todays exercises goal is to practice more on object oriented programming

### `Exercise 1` override

1. Create a class that has at least one method
2. Create a subclass that uses your class (1) as base class
3. In the subclass (2) you should override the method from (1)
4. Print a instance of (1) and (2) both calling the same method name

### `Exercise 2` menu

1. Create a class, i.e `Dog`, `Animal`, `Fridge`
2. Create a program that uses a menu
   1. The first option will create an object from your class
   2. The second option will print the object
   3. The third option will delete the object
3. If you try to print before creating an object or after deleted it, the program should print `No object available to print`
4. If you try to delete a object that doesn't exist, the program should print `No object to delete`

### `Exercise 3` composition vs inheritance

In this exercise you will write two alternative solutions, one with inheritance and one with composition.

#### Inheritance

1. Create a class named `Person`, it should have `address` stored, with street name, street number, postal code, country.
2. Create a class `Employee` that uses `Person´ as base class. Add employee number and salary.

#### Composition

1. Create a class `Address` with street name, street number, postal code, country.
2. Create a class `Employee` that has an address class, employee number and salary
