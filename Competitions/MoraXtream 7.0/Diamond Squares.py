T = int(input())

for i in range(T):
    state = 'NO'
    N = int(input())
    grid = []
    gridc = []
    gridinvc = []
    for i in range(N):
        grid.append(list(map(int,input().split())))
    for item in grid:
        gridc.append(item.count(1))

    ct = gridc.count(1)
    if ct==2 and ct+gridc.count(2)==N:
        for i in range(N):
            tot = 0
            for j in range(N):
                tot += grid[j][i]
            gridinvc.append(tot)
        ct = gridinvc.count(1)
        if ct==2 and ct+gridinvc.count(2)==N:
            state = 'YES'

    print(state)