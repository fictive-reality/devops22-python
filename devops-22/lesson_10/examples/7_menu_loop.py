
class Greetings:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello {self.name}")

    def say_goodbye(self):
        print(f"Goodbye {self.name}")


class Menu:

    MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'

1: 'Say hello',
2: 'Say goodbye',
3: 'Quit program'
"""

    def __init__(self, greeting):
        self.greeting = greeting

    def user_input(self):
        return int(input("Enter your choice [1-3]: "))

    def menu_choice(self, choice):
        if choice == 3:
            self.running = False
        elif choice == 1:
            self.greeting.say_hello()
        elif choice == 2:
            self.greeting.say_goodbye()

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)


if __name__ == '__main__':
    greeting = Greetings('Eva')
    Menu(greeting).menu_loop()
