'''
Code Wars Kata: https://www.codewars.com/kata/53dc54212259ed3d4f00071c

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: []
Output: 0

Input: [-2.398]
Output: -2.398

Assumptions
You can assume that you are only given numbers.
You cannot assume the size of the array.
You can assume that you do get an array and if the array is empty, return 0.
'''

def sum_array(a):
    # check if array is empty, and return 0 for the sum.
    if len(a) == 0:
        return 0
    else:
        return sum(a)
    
# Alternate solution after some reading
# The sum function is capable of reconciling an empty array

def sum_array2(a):
    return sum(a)
