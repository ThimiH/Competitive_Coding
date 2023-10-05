n,m,k = tuple(map(int,input().split()))

grid = {}

for z in range(k):
    i,a,b = tuple(map(int,input().split()))
    try:
        grid[i-1].update(list(range(a,b+1)))
    except:
        grid[i-1]=(set(range(a,b+1)))
rem = 0

for item in grid.values():
    rem += len(item)

print(n*m-rem)