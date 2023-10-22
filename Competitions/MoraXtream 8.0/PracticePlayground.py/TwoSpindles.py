from bisect import insort_left

n,k = tuple(map(int,input().split()))

disks = []

for _ in range(n):
    insort_left(disks,int(input()))

# 4pointers