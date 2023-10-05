n = int(input())
nums = sorted(list(map(int,input().split())))

dp = [1 for _ in range(n)]

for ind in range(n):
    if dp[ind]==1:
        ind_1 = ind
        ind_2 = ind+1
        while ind_2<n:
            if nums[ind_2]%nums[ind_1]:
                dp[ind_2]+=dp[ind_1]
                ind_1 = ind_2
            ind_2 += 1

print(max(dp))            