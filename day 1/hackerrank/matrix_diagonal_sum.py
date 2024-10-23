#!/bin/python3

"""
    https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true
"""

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    
    i = 0
    j = 0
    
    # you can use just one iterator, i know, because
    # both the values are gonna be same, but still, i wanna
    # do it this way
    while i <= len(arr) - 1 and j <= len(arr) - 1:
        left_diagonal += arr[i][j]
        i += 1
        j += 1
    
    i = 0
    j = len(arr) - 1
    
    while i <= len(arr) - 1 and j >= 0:
        right_diagonal += arr[i][j]
        i += 1
        j -= 1
    
    return abs(left_diagonal - right_diagonal)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
