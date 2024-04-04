'''
Code Wars Kata: https://www.codewars.com/kata/57a06b07cf1fa58b2b000252/train/python

Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.
'''

def is_it_letter(s):
    return s.isalpha()

# Alternate solution, using regex for practice
import re
def regex_letter(s):
    return True if re.search('[a-zA-Z]', s) else False