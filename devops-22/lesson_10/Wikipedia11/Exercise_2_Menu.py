# 1. Create a class, i.e `Dog`, `Animal`, `Fridge`
# 2. Create a program that uses a menu
#    1. The first option will create an object from your class
#    2. The second option will print the object
#    3. The third option will delete the object
# 3. If you try to print before creating an object or after deleted it, the program should print `No object available to print`
# 4. If you try to delete a object that doesn't exist, the program should print `No object to delete`


# ------------------------------------EXERCISE 1------------------------------------

# Create a class, i.e `Dog`, `Animal`, `Fridge`

class Dog:

    def __init__(self):
        self.food = 0

    def eat(self):
        self.food += 1

    def __str__(self):
        return f"I'm your best friend and my food level is ${self.food}"


# ------------------------------------EXERCISE 1------------------------------------

# Create a program that uses a menu

class Menu:

    MAIN_MENU_TEXT = """
    Welcome to this program!

    1. Create a new object
    2. Print your object
    3. Delete your object

    type q or Q to delete
    """

    def user_choice(self):
        return input("Enter your choice [1-3] or q: ")

    def wait_for_user(self):
        if self.running:
            input("Please press any key to continue.")

    def menu_commands(self, choice):
        if choice == "q" or choice == "Q":
            self.running = False
        elif choice == "1":
            self.dog = Dog()
        elif choice == "2":
            try:
                print(self.dog)
            except AttributeError:
                print("No object available to print")
                # Alternative to self.dog = None
    def start_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_choice()
            self.menu_commands(choice)
            self.wait_for_user()

Menu().start_loop()
