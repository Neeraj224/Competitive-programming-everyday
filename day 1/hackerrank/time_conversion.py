#!/bin/python3

# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hours = int(s[:2])
    mode = s[8:]
    
    if mode == "PM" and hours == 12:
        hours = 12
    if mode == "PM" and hours != 12:
        hours += 12
    if mode == "AM" and hours == 12:
        hours = 0
    
    if len(str(hours)) == 1 or hours == 0:
        new_s = '0'
    else:
        new_s = ''
        
    new_s += str(hours)
    new_s += s[2:8]
    
    return new_s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
