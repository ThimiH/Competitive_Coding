word_1 = input()
word_2 = word_1[::-1]

l = len(word_1)

dp = [[0]*(l+1) for _ in range(l+1)]

for i in range(l):
    for j in range(l):
        if word_1[i] == word_2[j]:
            dp[i][j] = max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[-2][-2])