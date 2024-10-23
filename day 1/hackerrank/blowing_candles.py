#!/bin/python3

# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_height = float('-inf')
    for i in range(len(candles)):
        max_height = max(max_height, candles[i])
    
    can_be_blown = 0
    for i in range(len(candles)):
        if candles[i] == max_height:
            can_be_blown += 1
    
    return can_be_blown

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
