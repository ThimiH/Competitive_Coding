a = input()
n = len(a)
b = input()
m = len(b)

dp = [[0]*n for _ in range(m)]

if a[0]==b[0]:
    dp[0][0] = 0
else:
    dp[0][0] = 1

for i in range(1,n):
    dp[0][i] = dp[0][i-1]+1

for i in range(1,m):
    dp[i][0] = dp[i-1][0]+1

for j in range(1,m):
    for i in range(1,n):
        if a[i] == b[j]:
            dp[j][i] = dp[j-1][i-1]
        else:
            dp[j][i] = min(dp[j-1][i],dp[j][i-1],dp[j-1][i-1])+1

print(dp[-1][-1])