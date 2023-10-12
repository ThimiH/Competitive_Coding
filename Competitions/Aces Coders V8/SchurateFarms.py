# Time fail

from bisect import insort_left,bisect_left

def position(x,y):
    n = x+y
    prev = (n*(n+1)//2)
    numb = prev + x
    return numb

rotten = []

for test in range(int(input())):
    line = input()
    x,y = tuple(map(int,line[2:].split()))
    if line[0]=="Q":
        print(position(x,y)-bisect_left(rotten,position(x,y)))
    elif line[0]=="R":
        insort_left(rotten,position(x,y))
    else:
        rotten.pop(bisect_left(rotten,position(x,y)))
