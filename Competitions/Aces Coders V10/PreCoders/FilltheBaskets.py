from bisect import bisect_right

n = int(input())
m = int(input())
balls = list(map(int,input().split()))
c = int(input())

balls=sorted(balls)

used = 0

while len(balls)>0:
    used += 1
    remaining = c
    while len(balls)>0 and remaining>=balls[0]:
        ind = bisect_right(balls,remaining)
        remaining -= balls.pop(ind-1)

print((n-used)*10)