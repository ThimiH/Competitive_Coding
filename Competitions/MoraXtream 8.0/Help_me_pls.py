# Optimize

for test in range(int(input())):
    l,p,q = tuple(map(int,input().split()))
    s = input()
    
    dp = [float("INF")]*l
    dp[0] = p

    for i in range(1,l):
        for j in range(i,i-(i+1)//2,-1):
            if s[j:i+1] in s[:j]:
                dp[i] = min(dp[i],dp[j-1]+p*(i-j+1),dp[j-1]+q)
            else:
                dp[i] = min(dp[i],dp[j-1]+p*(i-j+1))
                break
    
    print(dp[-1])

    
    
    
    # ans = p
    # i = 1
    # while i <l:
    #     add = 0
    #     for j in range(i+1,min(2*i+1,l+1)):
    #         if s[i:j] in s[:i]:
    #             if j == min(2*i,l):
    #                 ans += min(p*(j-i),q)
    #                 i = j
    #             else:
    #                 add = min(p*(j-i),q)
    #             continue
    #         else:
    #             if j == i+1:
    #                 ans += p
    #                 i=j
    #             else:
    #                 ans += add
    #                 i = j-1
    #             break
    #     print(s[:i],ans)
    # print(ans)