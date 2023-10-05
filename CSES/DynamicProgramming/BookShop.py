n,x = tuple(map(int,input().split()))
prices = list(map(int,input().split()))
pages = list(map(int,input().split()))

zipped_data = zip(prices,pages)

sorted_zipped_data = sorted(zipped_data, key = lambda x : x[0])

prices,pages = zip(*sorted_zipped_data)

dp = [[0]*(x+1) for _ in range(2)]

for j in range(1,n+1):
    for i in range(1,x+1):
        if i < prices[j-1]:
            pass
        else:    
            dp[1][i] = max(dp[0][i],dp[0][i-prices[j-1]]+pages[j-1])
    dp[0] = dp[1][:]


print(dp[0][x])