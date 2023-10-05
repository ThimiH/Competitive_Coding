#Tuple input
h,w = tuple(map(int,input().split()))

grid = []

for z in range(h):
    grid.append(list(map(int,input().split())))

ax = 0
ay = 0

for x in range(h):
    for y in range(w):
        if y == 0:
            ax += grid[x][0] + grid[x][w-1]
        else:
            ax += abs(grid[x][y]-grid[x][y-1])

for y in range(w):
    for x in range(h):
        if x == 0:
            ay += grid[0][y] + grid[h-1][y]
        else:
            ax += abs(grid[x][y]-grid[x-1][y])

print(ax+ay+h*w*2)