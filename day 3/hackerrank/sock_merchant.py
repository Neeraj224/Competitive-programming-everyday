#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, socks):
    # Write your code here
    sock_map = {}
    
    for sock in socks:
        if sock not in sock_map:
            sock_map[sock] = 1
        else:
            sock_map[sock] += 1
    
    pairs = 0
    
    for sock in sock_map.values():
        pairs += sock // 2
    
    return pairs
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    socks = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, socks)

    fptr.write(str(result) + '\n')

    fptr.close()
