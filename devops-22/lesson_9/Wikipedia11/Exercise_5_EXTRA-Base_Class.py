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

import random


# This class is the base class for the rest. Takes name and year of birth as input
class Person:
    def __init__(self, name, YoB):
        self.name = name
        self.YoB = YoB

# This is the player class which takes arguments from the class "Person". It also needs to have stats an aditional input
class Player(Person):
    def __init__(self, name, YoB, stats):
        super().__init__(name, YoB)
        self.stats = stats

# This method makes it so the name, YoB and stats of the player returns when the function is called
    def __str__(self):
        return f"{self.name} [{self.YoB}] - {self.stats}"
    
# Coach class, uses arguments from Person and also needs an aditional input for voice level
class Coach(Person):
    def __init__(self, name, YoB, voice_level):
        super().__init__(name, YoB)
        self.voice_level = voice_level
    
    def __str__(self):
        return self.name
    
# This class is where the main magic happens. I will generate stats for the player, takes a random int from 1 to 10.
# It also prints the name of the coach and returns the player names with thier stats
class Team:
    def __init__(self, players, coach):
        self.players = players
        self.coach = coach
    
    def summarize_team(self):
        team = """
-------------------------------------
-------------- My team --------------
-------------------------------------
"""
        team += f"Coach {self.coach}\n"
        team += "-------------- Players --------------\n"
        team += "\n".join(map(str, self.players))
        return team


def get_random_stats():
    return (
        random.randint(1, 10),
        random.randint(1, 10),
        random.randint(1, 10))

        
def main():
    coach = Coach("Fredrik", 1992, 5)
    
    players = []
    for name in ["Johanna", "Anduin", "Kiara", "Jesper", "Josephine", "Jessica", "Jacob", "Lotta", "Pia", "Peter", "Margareta"]:
        YoB = random.randint(1987, 2004)
        players.append(Player(name, YoB, get_random_stats()))
        
    team = Team(players, coach)
    print(team.summarize_team())


if __name__ == "__main__":
    main()
    
    
