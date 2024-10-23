#!/bin/python3

"""
    https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
"""

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    counter = n - 1
    SPACES = " "
    SYMBOL = "#"
    for i in range(n):
        for i in range(counter):
            print(SPACES, end = "")
        
        for i in range(n - counter):
            print(SYMBOL, end = "")
        
        print("")
        counter -= 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
