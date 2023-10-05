def checkmax(grid):
    ans = 0
    for i in range(20):
        for j in range(20):
            mult1=1
            mult2=1
            mult3=1
            mult4=1
            for k in range(4):
                if j<=16:
                    mult1 *= grid[i][j+k]
                if i<=16 and j<=16:
                    mult2 *= grid[i+k][j+k]
                if i<=16:
                    mult3 *= grid[i+k][j]
                if 3<=i and j<=16:
                    mult4 *= grid[i-k][j+k]
            if mult1>ans:
                ans=mult1
            if mult2>ans:
                ans=mult2
            if mult3>ans:
                ans=mult3
            if mult4>ans:
                ans=mult4
    print(ans)
    return None

def const(grid):
    for x in grid:
        for item in x:
            if 0<=item<=100:
                continue
            else:
                return False
    return True

grid=[]

for y in range(20):
    grid.append(list(map(int,input().split())))

if const(grid):
    checkmax(grid)