
# Print regnr with a method

class Car:

    def __init__(self, regnr):
        self.regnr = regnr

    def print_regnr(self):
        print(self.regnr)


# Call the method on a instance, NOT the class

volvo = Car("abc123")
volvo.print_regnr()  # abc123

# A function on a class
# Is called method in a instance

print(Car.print_regnr)  # <function Car.print_regnr at 0x1096f33a0>
print(volvo.print_regnr)
# <bound method Car.print_regnr of <__main__.Car object at 0x1096dfe80>>

# WARNING remember to use volvo.print_regnr() with the () in your code.

# A method can also take arguments


class Dog:

    def __init__(self, name, level=2):
        self.name = name
        self.level = level

    # function arguments
    def bark(self):
        sound = "woof"
        if self.level >= 3:
            sound = f"{sound.upper()}!!!!"
        print(sound)


# bark without arguments
badger = Dog("bill")
badger.bark()

# bark with level argument 5
golden = Dog("Buddy", 5)
golden.bark()
