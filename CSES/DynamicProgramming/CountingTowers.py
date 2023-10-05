n = 0
tests = []

for test in range(int(input())):
    m = int(input())
    n = max(n,m)
    tests.append(m)
MOD = 10**9+7

dp = [[0,0] for _ in range(n+1)]
dp[1] = [1,1]
for i in range(2,n+1):
    dp[i][0] = (dp[i-1][0]*4+dp[i-1][1])%MOD
    dp[i][1] = (dp[i-1][0]+dp[i-1][1]*2)%MOD

for test in tests:
    print((dp[test][0]+dp[test][1])%MOD)