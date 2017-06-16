#!/usr/bin/env python3
'''
Write a Python program, that will accept two tuples of 2 numbers
each representing coordinates (position) of a point and calculate
the distance between those 2 points. The output should be a float,
therefore let's round the result to 2 decimal places.

The distance should be straight line between the two points.
The coordinates cannot be negative numbers.



Example:

Input:
The point A is situated at coords [234, 34]
The point B is situated at coords [27, 114]

Output:
'''
# input points A,B between which is the distance we have to calculate
A=[234, 34]
B=[27, 114]

from math import sqrt

def main(A,B):
    # your program should use knowledge from basic school about
    # calculating the length of the 3rd side in a triangle
    # you will also need to use the function sqrt which is used as follows:
    # sqrt(25) -> result is 5
    a = round(A[0]-B[0],2)
    b = round(A[1] - B[1],2)
    result = round(sqrt(a**2 + b**2),2)

    print(result)
    return result

if __name__ == '__main__':
    dist = main(A,B)
