t = int(input())

for z in range(t):
    grid = {}
    n = int(input())
    powers = list(map(int,input().split()))
    for i in range(n):
        grid[i+1]=[powers[i],[]]
    for y in range(1,n):
        s,e = tuple(map(int,input().split()))
        if grid[s][0]>grid[e][0]:
            grid[s][1].append(e)
        elif grid[s][0]<grid[e][0]:
            grid[e][1].append(s)

powers.sort()
startlst = [[][:] for g in range(n)]
for value in grid.keys():
    if startlst[powers.index(grid[value][0])]==[]:
        startlst[powers.index(grid[value][0])].append(value)
    else:
        j = 0
        while True:
            if startlst[powers.index(grid[value][0])+j]==[]:
                startlst[powers.index(grid[value][0])+j].append(value)
                break
            else:
                j+=1

ans = 1

for item in startlst:
    print(grid[item])
    newls = grid[item][1]
    if newls==[]:
        grid[item].append(1)
    else:
        ansnew = 1
        for newone in newls:
            ansnew += grid[newone][2]
        if ansnew>ans:
            ans = ansnew

print (ans)