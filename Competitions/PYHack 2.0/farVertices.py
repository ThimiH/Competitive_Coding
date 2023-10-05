n,k = tuple(map(int,input().split()))

distance = [[float("inf")]*n for _ in range(n)]

for i in range(n):
    distance[i,i] = 0

for _ in range(n-1):
    x,y = tuple(map(int,input().split()))
    distance[x-1][y-1] = distance[y-1][x-1] = 1

for vertex in range(n):
    for x in range(n):
        for y in range(n):
            distance[x][y] = min(distance[x][y],distance[x][k]+distance[k][y])

