n,x = tuple(map(int,input().split()))
coins = list(map(int,input().split()))
mod = 10**9+7
dp = [0]*(x+1)
dp[0] = 1

for i in range(1,x+1):
    for coin in coins:
        if i>=coin:
            dp[i] = (dp[i]+dp[i-coin])%mod

print(dp[-1])