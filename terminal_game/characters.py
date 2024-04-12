from random import randint

'''
Establish character classes.
'''

class Hero(object):
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.health = self.max_health
        self.level = 1
        self.experience_to_level = 100
        self.experience = 0
        self.position_x = 0
        self.position_y = 0
        self.attack_speed = 1.0
        self.attack_modifier = 1.0

    def heal(self):
        healed = randint(5,9)

        if self.max_health < self.health + healed:
            self.health = self.max_health
            print(f"You healed yourself back to full health.")
        else:
            print(f"You healed yourself for {healed} points.")
            self.health += healed

        return

    def attack(self):
        return self.attack_modifier * randint(5,7)
    
    def level_up(self):
        self.level += 1
        self.max_health += 5
        self.attack_modifier += 0.1
        self.experience_to_level = self.experience_to_level * 2

        if self.level % 5 == 0:
            self.attack_speed += 0.2


class Goblin(object):
    def __init__(self):
        self.name = "goblin"
        self.health = 80
        self.damage = 5
        self.attack_speed = (randint(8, 12) / 10)

    def attack(self):
        return randint(3,8)