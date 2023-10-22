t = int(input())  # Number of test cases

for test in range(t):
    n = int(input())
    s = input()

    dp = [0] * (len(s) + 1)  # Initialize a dynamic programming array with mpz

    dp[0] = 1
    if int(s[0]) > 0 and int(s[0]) <= n:
        dp[1] = 1

    if n < 10:
        for num in range(1, len(s)):
            if int(s[num]) > 0 and int(s[num]) <= n:
                dp[num + 1] = dp[num] + dp[num - 1]
    else:
        for num in range(1, len(s)):
            if int(s[num]) > 0 and int(s[num]) <= n:
                dp[num + 1] = dp[num]

            combined = int(s[num - 1] + s[num])
            if combined >= 10 and combined <= n:
                dp[num + 1] += dp[num - 1]

    print(dp[len(s)])


# for test in range(int(input())):
#     n = int(input())
#     s = input()
#     dp = [1]
#     if 0<int(s[0])<=n:
#         dp.append(1)
#     else:
#         dp.append(0)

#     if n<10:
#         for num in range(1,len(s)):
#             if 0<int(s[num])<=n:
#                 dp.append(dp[num-1])
#             else:
#                 dp.append(0)
#     else:
#         for num in range(1,len(s)):
#             if 0<int(s[num])<=n:
#                 dp.append(dp[-1])
#             else:
#                 dp.append(0)
            
#             if 0<int(s[num-1]+s[num])<=n:
#                 dp[-1]+=dp[-3]

#     print(dp[-1])

