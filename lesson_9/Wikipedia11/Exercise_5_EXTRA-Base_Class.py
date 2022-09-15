# 1. Create a class `Person`
    # 1. A person has a name
    # 2. A person has a year of birth
# 2. Create a class `Player` that uses `Person` as a base
    # 1. A player has speed 1-10
    # 2. A player has agility 1-10
    # 3. A player has strength 1-10
# 3. Create a class `Coach` that uses `Person` as a base
#    1. A couch has a voice_level 1-10
# 4. Create a class `Team`
#    1. A team has players in a list
#    2. A team has a coach
#    3. Write a method that can summarize the team composition.

class Person:
    def __init__(self, name, YoB):
        self.name = name
        self.YoB = YoB

class Player(Person):
    def __init__(self, name, YoB, Speed, Agility, Strenght):
        super().__init__(name, YoB)
        self.speed = Speed
        self.agility = Agility
        self.strenght = Strenght

class Coach(Person):
    def __init__(self, name, YoB, voice_level):
        super().__init__(name, YoB)
        self.voice_level = voice_level

class Team:
    def __init__(self, players, coach):
        self.players = players
        self.coach = coach