n = int(input())
mod = 10**9+7

dp = [0 for _ in range(n)]

for i in range(min(6,n)):
    dp[i] = 1

for j in range(1,n):
    for k in range(min(j,6)):
        dp[j] = (dp[j]+dp[j-1-k])
    dp[j] = dp[j]%mod

print(dp[-1])