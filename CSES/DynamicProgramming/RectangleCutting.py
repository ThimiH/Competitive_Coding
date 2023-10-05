a,b = tuple(map(int,input().split()))
moves = 0

dp = [[float("INF")]*a for _ in range(b)]

for i in range(a):
    dp[0][i] = i

for i in range(b):
    dp[i][0] = i

for j in range(1,b):
    for i in range(1,a):
        if i == j:
            dp[j][i] = 0
        else:
            for n in range(1,a//2):
                dp[j][i] = min(dp[j][i],dp[j][n]+dp[j][i-n-1]+1)
            for m in range(1,b//2):
                dp[j][i] = min(dp[j][i],dp[m][i]+dp[j-m-1][i]+1)

print(dp[-1][-1])    