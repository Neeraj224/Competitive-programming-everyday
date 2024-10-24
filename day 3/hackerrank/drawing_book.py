#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    if p == 1 or p == n:
        return 0
    if n % 2 == 0 and p == n - 1:
        return 1
        
    start = 0
    end = 0
    
    if p % 2 == 0:
        # check from start
        i = 2
        start += 1
        while i != p:
            i += 2
            start += 1
        
        # check from the end:
        # if we have even number of pages:
        if n % 2 == 0:
            j = n
            while j != p:
                j -= 2
                end += 1
        # if we have odd number of pages
        elif n % 2 != 0:
            j = n - 1
            while j != p:
                j -= 2
                end += 1
        
    elif p % 2 != 0:
        # check from start
        i = 1
        while i != p:
            i += 2
            start += 1
        
        # now check from the end:
        # if the number of pages are even:
        if n % 2 == 0:
            j = n - 1
            end += 1
            while j != p:
                j -= 2
                end += 1
        # if the number of pages are odd:
        elif n % 2 != 0:
            j = n
            while j != p:
                j -= 2
                end += 1
    
    return min(start, end)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
