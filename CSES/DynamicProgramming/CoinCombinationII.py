n,x = tuple(map(int,input().split()))
coins = list(map(int,input().split()))
MOD = 10**9+7
dp = [0]*(x+1)
dp[0] = 1

for coin in coins:
    for i in range(x+1-coin):
        dp[i+coin] = (dp[i+coin]+dp[i])%MOD

print(dp[-1])