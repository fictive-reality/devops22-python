import sys
from time import sleep


class App:

    main_menu_text = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'

1: 'Single player',
2: 'Multiplayer',
3: 'Quit program'
"""

    def __init__(self):
        self.run = False
        self.main_menu_commands = {1: self.cmd_single_player,
                                   2: self.cmd_multiplayer, 3: self.quit}

    def setup(self, options):
        print(f'fake setup for {options}')

    def fake_play(self, text):
        print(text, end='', flush=True)
        for i in range(5):
            sleep(1)
            print('.', end='', flush=True)
        print('\nDone playing')

    def cmd_single_player(self):
        self.fake_play('Playing single player ')

    def cmd_multiplayer(self):
        self.fake_play('Playing multiplayer player ')

    def quit(self):
        print('Shutting down')
        self.run = False
        sys.exit(0)

    def main_menu(self):
        print(f'{App.main_menu_text}')

    def execute_command(self, menu, choice):
        try:
            menu[choice]()
        except Exception as e:
            print(e)
            print('something went wrong')

    def start_loop(self):
        self.run = True
        while self.run:
            self.main_menu()
            choice = int(input('Enter your choice [1-3]: '))
            self.execute_command(self.main_menu_commands, choice)
