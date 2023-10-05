n = str(int(input()))

dp = [1 for _ in range(len(n))]

for i in range(len(n)-2,-1,-1):
    dp[i]+=dp[i+1]*2

ans = 0
add = True

for i in range(len(n)):
    if int(n[i]):
        if add:
            ans += dp[i]
            add = False
        else:
            ans -= dp[i]
            add = True

print(ans)

## How can this work