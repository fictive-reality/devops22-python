# In your class create a `__init__`function, i.e

# class MyClass:
    
    # def __init__(self, my_arg):
        # self.my_arg = my_arg

# 1. Create a class Animal with a `__init__` that takes 1 argument
# 2. Create a class Dog with a `__init__` that takes 2 arguments
# 3. Create a class Supermarket with a `__init__` that takes 3 arguments
# 4. Create a class Coop with a `__init__` that takes 4 arguments

    # To test your code, you can create a main

    # class MyCLass:
        # pass


    # if __name__ == '__main__':
        # my_class = MyClass("my_string")

# <div class="page"/>


# ------------------------------------EXERCISE 1------------------------------------

class Animal:
    def __init__(self, type):
        self.type = type

# ------------------------------------EXERCISE 2------------------------------------

class Dog:
    def __init__(self, breed, size):
        self.breed = breed
        self.size = size

# ------------------------------------EXERCISE 3------------------------------------

class Supermarket:
    def __init__(self, store, products, employees):
        self.store = store
        self.products = products
        self.employees = employees

# ------------------------------------EXERCISE 4------------------------------------

class Coop:
    def __init__(self, location, size):
        self.location = location
        self.size = size

if __name__ == "__main__":
    Animal_test = Animal("Cat")

print(Animal_test.type)