#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    most_sightings = []
    
    freq_map = {}
    
    for bird_id in arr:
        if bird_id not in freq_map:
            freq_map[bird_id] = 1
        else:
            freq_map[bird_id] += 1
    
    max_freq = max(freq_map.values())
    
    for key, val in freq_map.items():
        if val == max_freq:
            most_sightings.append(key)
    
    return min(most_sightings)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
