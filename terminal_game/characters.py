'''
Establish character classes.
'''

class Hero(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 5
        self.experience = 0
        self.position_x = 0
        self.position_y = 0