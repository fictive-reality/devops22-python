from cmd import Cmd


class AmazinGame(Cmd):
    intro = 'Welcome to the Amazing game.\tType help or ? to list commands.\n'
    prompt = '(game) '

    def do_forward(self, arg):
        'Move forward by the specified distance:  FORWARD 10'
        print(f'Going forward {arg} steps')

    def do_right(self, arg):
        'Turn right by given number of degrees:  RIGHT 20'
        print(f'Turn Right {arg} steps')

    def do_left(self, arg):
        'Turn left by given number of degrees:  LEFT 90'
        print(f'Turn left {arg} steps')

    def do_home(self, arg):
        'Return to the home position:  HOME'
        print('Returned home')

    def do_bye(self, arg):
        'Stop the game and exit:  BYE'
        print('Thank you for using Amazing game')
        return True

    def precmd(self, line):
        line = line.lower()
        return line


if __name__ == '__main__':
    AmazinGame().cmdloop()
