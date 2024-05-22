n,m = tuple(map(int,input().split()))
l_1 = list(map(int,input().split()))
l_2 = list(map(int,input().split()))

dp = [[0]*n for _ in range(m)]
dp2 = [[0]*n for _ in range(m)]

for i in range(n):
    if l_2[0] == l_1[i]:
        dp[0][i] = 1
        dp2[0][i] = l_2[0]
    else:
        dp[0][i] = dp[0][i-1]
        dp2[0][i] = dp2[0][i-1]

for j in range(m):
    if l_1[0] == l_2[j]:
        dp[j][0] = 1
        dp2[j][0] = l_1[0]
    else:
        dp[j][0] = dp[j-1][0]
        dp2[j][0] = dp2[j-1][0]

for i in range(1,n):
    for j in range(1,m):
        if l_1[i] == l_2[j]:
            dp[j][i] = dp[j-1][i-1]+1
            dp2[j][i] = l_1[i]
        elif dp[j-1][i] <= dp[j][i-1]:
            dp[j][i] = dp[j][i-1]
            dp2[j][i] = dp2[j][i-1]
        else:
            dp[j][i] = dp[j-1][i]
            dp2[j][i] = dp2[j-1][i]



val = 0

# for line in dp:
#     print(line)

# print()

# for line in dp2:
#     print(line)

for i,x in enumerate(dp):
    if x[-1] != val:
        print(dp2[i][-1], end=" ")
        val = x[-1]


