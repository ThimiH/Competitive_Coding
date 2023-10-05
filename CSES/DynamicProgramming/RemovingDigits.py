n = int(input())

dp = [float("INF") for _ in range(n+1)]

for ind in range(n+1):
    if ind<10:
        dp[ind] = 1
    else:
        for digit in set(str(ind)):
            dp[ind] = min(dp[ind],dp[ind-int(digit)]+1)

print(dp[-1])