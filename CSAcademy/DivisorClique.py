n = int(input())
nums = sorted(list(map(int,input().split())))

dp = [1 for _ in range(n)]

for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if nums[j]%nums[i]==0:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))            