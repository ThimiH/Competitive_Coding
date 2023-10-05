#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'playWithWords' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def playWithWords(s):
    length = len(s)
    firsts = []
    seconds = []
    lens = []
    ans = 1
    for first in range(length):
        for second in range(first+1,length):
            if s[first:second+1] == s[first:second+1][::-1]:
                firsts.append(first)
                seconds.append(second)
                lens.append(second-first+1)
    
    ind1, ind2 =0,0
    while ind2<len(lens):
        while firsts[ind1]<=seconds[ind2]:
            ind1 += 1
            if ind1 == len(firsts):
                break
        try :
            ans = max(ans, max(lens[:ind2+1])*max(lens[ind1:]))
        except:
            break
        ind2+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = playWithWords(s)

    fptr.write(str(result) + '\n')

    fptr.close()
