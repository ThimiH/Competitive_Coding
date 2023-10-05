T = int(input())

def takein():
    return list(map(int,input().split()))

for z in range(T):
    N,M = tuple(takein())
    grid = []
    for y in range(N):
        lev = takein()
        grid.append([min(lev),max(lev)])

print(grid)