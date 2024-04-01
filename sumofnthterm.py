'''
Code Wars Kata: https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

Task
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

You will need to figure out the rule of the series to complete this.

Rules
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.

Examples (Input --> Output)
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"



Resources I found for the formatting:

https://docs.python.org/3/tutorial/inputoutput.html

https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python

'''



def series_sum(n):
    # First eliminate 0 from the pattern
    if n == 0:
        return "0.00"
    else:
        # If n = 1, then the return is 1.
        result = 1
        # Use an iterator to keep track of where in the sequence you are.
        i = 1
        
        while i < n:
            # Based on the examples given, the pattern at n = 2 is adding 1/4 and every additional iteration is 1/(4 + 3(n-1)).
            result += 1/(4 + ((i-1)*3))
            i += 1
        # Once the result is determined, we format it at 2 decimal places as a string.
        return "{:0.2f}".format(result)