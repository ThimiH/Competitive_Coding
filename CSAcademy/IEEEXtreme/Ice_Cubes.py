for test in range(int(input())):
    n,m,k,b =  tuple(map(int,input().split()))
    dp = [[[0]*k for __ in range(m)] for _ in range(n)]
    grid = []
    for line in range(n):
        grid.append(list(map(int,input().split())))
    
    if grid[0][0] < b:
        if k > 1:
            dp[0][0][1] = grid[0][0]
    else:
        dp[0][0][0] = grid[0][0]
    
    for q in range(1,m):
        for r in range(k):
            if dp[0][q-1][r]:
                if grid[0][q] < b:
                    if r+1 < k:
                        dp[0][q][r+1] = max(dp[0][q][r+1],dp[0][q-1][r]+grid[0][q])
                else:
                    dp[0][q][0] = max(dp[0][q][0],dp[0][q-1][r]+grid[0][q])

    for p in range(1,n):
        for r in range(k):
            if dp[p-1][0][r]:
                if grid[p][0] < b:
                    if r+1 < k:
                        dp[p][0][r+1] = max(dp[p][0][r+1],dp[p-1][0][r]+grid[p][0])
                else:
                    dp[p][0][0] = max(dp[p][0][0],dp[p-1][0][r]+grid[p][0])

    for p in range(1,n):
        for q in range(1,m):
            for r in range(k):
                if dp[p][q-1][r]:
                    if grid[p][q] < b:
                        if r+1 < k:
                            dp[p][q][r+1] = max(dp[p][q][r+1],dp[p][q-1][r]+grid[p][q])
                    else:
                        dp[p][q][0] = max(dp[p][q][0],dp[p][q-1][r]+grid[p][q])
                if dp[p-1][q][r]:
                    if grid[p][q] < b:
                        if r+1 < k:
                            dp[p][q][r+1] = max(dp[p][q][r+1],dp[p-1][q][r]+grid[p][q])
                    else:
                        dp[p][q][0] = max(dp[p][q][0],dp[p-1][q][r]+grid[p][q])

    answer = -1
    for r in range(k):
        answer = max(dp[-1][-1][r],answer)

    if answer:
        print('Case %i: %i' %((test+1),answer))
    else:
        print('Case %i: IMPOSSIBLE' %(test+1))