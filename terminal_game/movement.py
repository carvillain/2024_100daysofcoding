from characters import *

'''
Movement is viewed from a topdown perspective.

North increases the y position coordinate.
South decreases the y position coordinate.
East increases the x position coordinate.
West decreases the x position coordinate.

The diagonal directions, ie northeast, impact both the x and y coordinates simultaneously.
'''


def move_north(self):
    self.position_y += 1
    return

def move_north_east(self):
    self.position_y += 1
    self.position_x += 1
    return

def move_north_west(self):
    self.position_y += 1
    self.position_x -= 1
    return

def move_south(self):
    self.position_y -= 1
    return

def move_south_east(self):
    self.position_y -= 1
    self.position_x += 1
    return

def move_south_west(self):
    self.position_y -= 1
    self.position_x -= 1
    return 

def move_east(self):
    self.position_x += 1
    return

def move_west(self):
    self.position_x -= 1
    return