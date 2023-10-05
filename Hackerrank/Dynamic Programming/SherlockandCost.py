#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # 1 or number could have been selected.
    selectedbi = selected1 = 0
    selectbi = select1 = 0
    for index in range(1,len(B)):
        selectbi = max(selectedbi+abs(B[index]-B[index-1]),selected1+abs(B[index]-1))
        select1 = selectedbi + (B[index-1] -1)
        
        selectedbi = selectbi
        selected1 = select1
    
    return max(selected1,selectedbi)
    
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
