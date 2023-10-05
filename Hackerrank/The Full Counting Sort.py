#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    n = len(arr)
    lst = [[] for i in range(100)]
    for x in range(n//2):
        lst[int(arr[x][0])].append('-')
    for x in range(n//2,n):
        lst[int(arr[x][0])].append(arr[x][1])
        
    for item in lst:
        if item:
            print(*item,end=' ')
    return None

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)