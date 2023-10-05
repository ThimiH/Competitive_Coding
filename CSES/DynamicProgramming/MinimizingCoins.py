from math import isinf

n,x = tuple(map(int,input().split()))
coins = list(map(int,input().split()))

dp = [float('INF')]*(x+1)
dp[0] = 0

for i in range(1,x+1):
    for coin in coins:
        if i>=coin:
            dp[i] = min(dp[i],dp[i-coin]+1)

if isinf(dp[-1]):
    print(-1)
else:
    print(dp[-1])