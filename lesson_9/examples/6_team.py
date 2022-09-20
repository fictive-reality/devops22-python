class Person:

    def __init__(self, name) -> None:
        self.name = name


class Player(Person):
    pass


class Coach(Person):
    pass


class Team:

    def __init__(self):
        self.coach = None
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def switch_coach(self, coach):
        self.coach = coach


madrid = Team()
roma = Team()

roma.add_player(Player("Ida Svedberg"))
roma.switch_coach(Coach("Svennis"))

print(madrid.players)
print(roma.players)
