x,y,z = tuple(map(int,input().split()))
grid = []
for _ in range(x):
    grid.append(list(map(int,input().split())))

def desemble(x,y,grid):
    parts = []
    for i in range(min(x,y)//2):
        parts.append([])
        for j in range(i,y-i-1):
            parts[i].append(grid[i][j])
        for j in range(i,x-i-1):
            parts[i].append(grid[j][-1-i])
        for j in range(y-i-1,i,-1):
            parts[i].append(grid[-i-1][j])
        for j in range(x-i-1,i,-1):
            parts[i].append(grid[j][i])
    return parts

def assemble(x,y,parts,grid):
    for i in range(min(x,y)//2):
        for j in range(i,y-i-1):
            grid[i][j]=parts[i][0]
            parts[i].pop(0)
        for j in range(i,x-i-1):
            grid[j][-1-i]=parts[i][0]
            parts[i].pop(0)
        for j in range(y-i-1,i,-1):
            grid[-i-1][j]=parts[i][0]
            parts[i].pop(0)
        for j in range(x-i-1,i,-1):
            grid[j][i]=parts[i][0]
            parts[i].pop(0)
    return grid

parts = desemble(x,y,grid)

for i,arr in enumerate(parts):
    arr2 = arr[z%len(arr):]+arr[:(z%len(arr))]
    parts[i] = arr2[:]    
    
grid = assemble(x,y,parts,grid)

for line in grid:
    print(" ".join(map(str,line)))