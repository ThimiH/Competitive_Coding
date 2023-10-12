n,k = tuple(map(int,input().split()))
arr = list(map(int,input().split()))
arr = sorted(arr)

dp = [0]*(n+1)

for i in range(n):
    if dp[i]==0:
        for j in arr:
            if i+j>n:
                break
            dp[i+j] = 1

for i in dp[1:]:
    if i:
        print("W", end = "")
    else:
        
        print("L", end = "")