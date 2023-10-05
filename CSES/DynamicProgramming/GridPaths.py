n = int(input())
grid = []
for _ in range(n):
    grid.append(list(input()))

MOD = 10**9+7

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j]=='*':
            pass
        else:
            if i == 0:
                if j == 0:
                    dp[i][j] = 1
                else :
                    dp[i][j] = dp[i][j-1]
            elif j == 0 :
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i-1][j]+dp[i][j-1])%MOD

print(dp[-1][-1])