'''
Code Wars Kata: https://www.codewars.com/kata/581214d54624a8232100005f/train/python

Function receive a two-dimensional square array of random integers. On the main diagonal, all the negative integers must be changed to 0, while the others must be changed to 1 (Note: 0 is considered non-negative, here).

(You can mutate the input if you want, but it is a better practice to not mutate the input)

Example:

Input array

[
  [-1,  4, -5, -9,  3 ],
  [ 6, -4, -7,  4, -5 ],
  [ 3,  5,  0, -9, -1 ],
  [ 1,  5, -7, -8, -9 ],
  [-3,  2,  1, -5,  6 ]
]
Output array

[
  [ 0,  4, -5, -9,  3 ],
  [ 6,  0, -7,  4, -5 ],
  [ 3,  5,  1, -9, -1 ],
  [ 1,  5, -7,  0, -9 ],
  [-3,  2,  1, -5,  1 ]
]
'''


def matrix(array): 
    # Iterate through each list in the matrix
    for i in range(0,len(array)):
        # The position of each list in the array corresponds with the 
        # position inside the list for the value to be modified
        if array[i][i] >= 0:
            array[i][i] = 1
        else:
            array[i][i] = 0
    
    return array