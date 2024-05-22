n,k = tuple(map(int,input().split()))

grid = [1]*(n//2+1)
mod = 10**9+7
for i in range(1,n//2+1):
    grid[i]=(grid[i-1]*((2*i-1)%mod)*((2*i)%mod)*pow(i,mod-2,mod)*pow(i+1,mod-2,mod))%mod

dp = [0]*(n+1)
dp[0] = 1

for i in range(n):
    dp[i+1] = (dp[i+1]+dp[i])%mod
    for j in range(k):
        ind = i+(j+1)*2
        if ind > n:
            break
        dp[ind] = (dp[ind]+dp[i]*grid[j])%mod

print(dp[-1])