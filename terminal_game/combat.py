'''
Codewars Kata: https://www.codewars.com/kata/586c1cf4b98de0399300001d/train/python

Create a combat function that takes the player's current health 
and the amount of damage recieved, and returns the player's new 
health. Health can't be less than 0.

'''

def combat(health, damage):
    return 0 if damage > health else health - damage