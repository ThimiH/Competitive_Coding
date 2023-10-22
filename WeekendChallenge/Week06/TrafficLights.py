#Optimize

from bisect import insort_left

x,n = tuple(map(int,input().split()))
lights = list(map(int,input().split()))

points = [0,x]

for ind,light in enumerate(lights):
    insort_left(points,light)
    gap = 0
    for i in range(ind+2):
        gap = max(gap,points[i+1]-points[i])
    print(gap, end = " ")