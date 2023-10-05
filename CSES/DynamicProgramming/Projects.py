n = int(input())

dp = []

for _ in range(n):
    dp.append(list(map(int,input().split())))

def condition(arr):
    return (arr[1],arr[2])

dp = sorted(dp,key = condition)

for index in range(1,n):
    startdate = dp[index][0]
    upper = index - 1
    lower = 0
    while upper>lower:
        mid = (upper+lower)//2
        if startdate <= dp[mid][1]:
            upper = mid-1
        else :
            lower = mid+1
    job = lower
    if startdate > dp[job][1]:
        dp[index][2] = max(dp[index][2]+dp[job][2],dp[index-1][2])
    else:
        dp[index][2] = max(dp[index][2],dp[index-1][2])
    print(upper,lower,dp)
print(dp[-1][2])