for test in range(int(input())):
    n = int(input())
    colours = list(map(int,input().split()))
    dp = [[[500]*21 for _ in range(21)] for __ in range(n+1)]
    avl = [[[0]*21 for _ in range(21)] for __ in range(n+1)]
    dp[0][0][0] = 0
    avl[0][0][0] = 1
    for i in range(n):
        for p_1 in range(21):
            for p_2 in range(21):
                if avl[i][p_1][p_2]:
                    if p_1 == colours[i] or p_2 == colours[i]:
                        dp[i+1][p_1][p_2] = min(dp[i][p_1][p_2],dp[i+1][p_1][p_2])
                        avl[i+1][p_1][p_2] = 1
                    else:
                        dp[i+1][p_1][colours[i]] = min(dp[i][p_1][p_2]+1,dp[i+1][p_1][colours[i]])
                        avl[i+1][p_1][colours[i]] = 1
                        dp[i+1][colours[i]][p_2] = min(dp[i][p_1][p_2]+1,dp[i+1][colours[i]][p_2])
                        avl[i+1][colours[i]][p_2] = 1

    ans = 500
    for p_1 in range(21):
        for p_2 in range(21): 
            if avl[-1][p_1][p_2]:
                if dp[-1][p_1][p_2]<ans:
                    ans = dp[-1][p_1][p_2]
    
    print(ans)