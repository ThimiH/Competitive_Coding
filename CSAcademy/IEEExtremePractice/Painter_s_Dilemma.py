def row(x,y):
    return (x)*21+y

for test in range(int(input())):
    n = int(input())
    seq = list(map(int, input().split()))
    dp = [[float('inf') for i in range(n)] for j in range(21**2)]
    dp[row(0,seq[0])][0] = 1
    for i in range(n-1):
        for j in range(21**2):
            x = j//21
            y = j%21
            if dp[j][i] > 0 :
                if y == 0:
                    dp[row(x,seq[i+1])][i+1] = min(dp[j][i]+1,dp[row(x,seq[i+1])][i+1])
                    # print(1,i,x,y,seq[i+1],dp[j][i],dp[row(x,seq[i+1])][i+1])
                else:
                    if x == seq[i+1]:
                        dp[j][i+1] = min(dp[j][i+1],dp[j][i])
                        # print(2,i,x,y,seq[i+1],dp[j][i],dp[j][i+1])
                    else:
                        dp[row(seq[i+1],y)][i+1] = min(dp[j][i]+1,dp[row(seq[i+1],y)][i+1])
                        # print(3,i,x,y,seq[i+1],dp[j][i],dp[row(seq[i+1],y)][i+1])
                    if y == seq[i+1]:
                        dp[j][i+1] = min(dp[j][i+1],dp[j][i])
                        # print(4,i,x,y,seq[i+1],dp[j][i],dp[j][i+1])
                    else:
                        dp[row(x,seq[i+1])][i+1] = min(dp[j][i]+1,dp[row(x,seq[i+1])][i+1])
                        # print(5,i,x,y,seq[i+1],dp[j][i],dp[row(x,seq[i+1])][i+1])
    ans = n
    for i in range(21**2):
        ans = min(ans,dp[i][n-1])

    print(ans)
                    
