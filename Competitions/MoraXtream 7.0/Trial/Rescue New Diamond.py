N,H,M = tuple(map(int,input().split()))

heat = 0
grid = [[]]

for bar in range(1,N+1):
    heat+=bar
    grid[-1].append(bar)
    if len(grid[-1])>M or heat>H:
        print(bar)
        heat=bar
        grid[-1].remove(bar)
        grid.append([])        
        grid[-1].append(bar)
        print(grid)

print(len(grid))

for item in grid:
    item = list(map(str,item))
    print(' '.join(item))