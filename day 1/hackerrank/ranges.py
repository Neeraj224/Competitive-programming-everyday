#!/bin/python3

"""
    https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    
    negatives = 0
    positives = 0
    neutrals = 0
    
    for num in arr:
        if num == 0:
            neutrals += 1
        elif num < 0:
            negatives += 1
        else:
            positives += 1
    
    print("{:.6f}".format(positives / n))
    print("{:.6f}".format(negatives / n))
    print("{:.6f}".format(neutrals / n))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
