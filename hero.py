'''
Codewars Kata: https://www.codewars.com/kata/55e8aba23d399a59500000ce/train/python

Terminal Game - Create Hero Prototype
In this first kata in the series, you need to define a Hero prototype to be used in a terminal game. The hero should have the following attributes:

attribute	value
name	user argument or 'Hero'
position	'00'
health	100
damage	5
experience	0
'''

class Hero(object):
    def __init__(self, name = 'Hero'):
        #Add default values here
        self.name = name
        self.health = 100
        self.damage = 5
        self.experience = 0
        self.position = '00'