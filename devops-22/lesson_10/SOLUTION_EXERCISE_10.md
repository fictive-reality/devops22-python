# Exercise Lesson 10

## Instructions

Todays exercises goal is to practice more on object oriented programming

### `Exercise 1` override

1. Create a class that has at least one method

    ```python
    class Bicycle:

        def __init__(self):
            self.speed = 2

        def accelerate(self):
            self.speed += 1

        def slow(self):
            self.speed -= 1
    ```

2. Create a subclass that uses your class (1) as base class

    ```python
    class MTB(Bicycle):
        pass
    ```

3. In the subclass (2) you should override the method from (1)

    ```python
    class MTB(Bicycle):

        def slow(self):
            self.speed -= 1.2
    ```

4. Print a instance of (1) and (2) both calling the same method name

    ```python
    bicycle = Bicycle()
    bicycle.slow()
    print(bicycle.speed)

    mtb = MTB()
    mtb.slow()
    print(mtb.speed)
    ```

<div class="page"/>

### `Exercise 2` menu

1. Create a class, i.e `Dog`, `Animal`, `Fridge`
2. Create a program that uses a menu
   1. The first option will create an object from your class
   2. The second option will print the object
   3. The third option will delete the object
3. If you try to print before creating an object or after deleted it, the program should print `No object available to print`
4. If you try to delete a object that doesn't exist, the program should print `No object to delete`

    ```python

    class Dog:
        def __init__(self):
            self.food = 0

        def eat(self):
            self.food += 1

        def __str__(self):
            return f"I'm your best friend and my food level is ${self.food}"

    class Dog:
        def __init__(self):
            self.food = 0

        def eat(self):
            self.food += 1

        def __str__(self):
            return f"I'm your best friend and my food level is ${self.food}"

    class Menu:

        MAIN_MENU_TEXT = """
        Welcome to this program!

        1. Create a new object
        2. Print your object
        3. Delete your object
        
        type q or Q to delete
        """

        def user_choice(self):
            return input("Enter your choice 1-3 or q: ")

        def wait_for_user(self):
            if self.running:
                input("Please press any key to continues.")

        def menu_commands(self, choice):
            if choice == 'q' or choice == 'Q':
                self.running = False
            elif choice == "1":
                self.dog = Dog()
            elif choice == "2":
                try:
                    print(self.dog)
                except AttributeError:
                    print("No object available to print")
            elif choice == "3":
                try:
                    del self.dog
                except AttributeError:
                    print("No object to delete")
                    # Alternative self.dog = None

        def start_loop(self):
            self.running = True
            while self.running:
                print(Menu.MAIN_MENU_TEXT)
                choice = self.user_choice()
                self.menu_commands(choice)
                self.wait_for_user()

    Menu().start_loop()
    ```

<div class="page"/>

## `Exercise 3` composition vs inheritance

In this exercise you will write two alternative solutions, one with inheritance and one with composition.

### Inheritance

1. Create a class named `Person`, it should have `address` stored, with street name, street number, postal code, country.

2. Create a class `Employee` that uses `Person´ as base class. Add employee number and salary.

    ```python
    class Person:
        def __init__(self, street_name, postal_code, country):
            self.street_name = street_name
            self.postal_code = postal_code
            self.country = country


    class Employee(Person):
        def __init__(self, street_name, postal_code, country, emp_number, salary):
            super().__init__(street_name, postal_code, country)
            self.emp_number = emp_number
            self.salary = salary

        def __str__(self):
            return f"emp {self.emp_number} live on {self.street_name}"


    emp = Employee("Sveavägen", "11350", "Sweden", 1, 10000)
    print(emp)
    ```

<div class="page"/>

### Composition

1. Create a class `Address` with street name, street number, postal code, country.
2. Create a class `Employee` that has an address class, employee number and salary

    ```python
    class Address:
        def __init__(self, street_name, postal_code, country):
            self.street_name = street_name
            self.postal_code = postal_code
            self.country = country


    class Employee:
        def __init__(self, address, emp_number, salary):
            self.address = address
            self.emp_number = emp_number
            self.salary = salary

        def __str__(self):
            return f"emp {self.emp_number} live on {self.address.street_name}"


    address = Address("Sveavägen", "11350", "Sweden")
    emp = Employee(address, 1, 10000)
    print(emp)
    ```
