n,m = tuple(map(int,input().split()))
given = list(map(int,input().split()))
MOD = 10**9+7

dp = [[0]*(n) for _ in range(m+1)]

if given[0]:
    dp[given[0]][0]=1
else:
    for i in range(1,m+1):
        dp[i][0] = 1

for i in range(1,n):
    if given[i]:
        if given[i] == 1:
            dp[1][i] = (dp[1][i-1]+dp[2][i-1])%MOD
        elif given[i] == m:
            dp[m][i] = (dp[m][i-1]+dp[m-1][i-1])%MOD
        else:
            dp[given[i]][i] = (dp[given[i]][i-1]+dp[given[i]-1][i-1]+dp[given[i]+1][i-1])%MOD
    else:
        for j in range(1,m+1):
            if j == 1:
                dp[1][i] = (dp[1][i-1]+dp[2][i-1])%MOD
            elif j == m:
                dp[m][i] = (dp[m][i-1]+dp[m-1][i-1])%MOD
            else:
                dp[j][i] = (dp[j][i-1]+dp[j-1][i-1]+dp[j+1][i-1])%MOD

ans = 0

for i in range(m+1):
    ans += dp[i][-1]

print(ans%MOD)