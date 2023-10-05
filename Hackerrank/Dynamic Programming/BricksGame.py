#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bricksGame' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def bricksGame(arr):
    arr = arr[::-1]
    length = len(arr)
    dp = [0]*length
    total = 0
    for index in range(length):
        total += arr[index]
        if index<3:
            dp[index] = total
        else:
            dp[index] = max(total-dp[index-1],total-dp[index-2],total-dp[index-3])
        
    return dp[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()