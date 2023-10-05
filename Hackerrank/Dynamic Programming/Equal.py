for test in range(int(input())):
    n = int(input())
    nums = list(map(int,input().split()))
    m = min(nums)
    ans = [0]*3
    for i in range(3):
        for num in nums:
            num -= m-i
            ans[i]+=num//5
            num%=5
            ans[i]+=num//2
            ans[i]+=num%2
    print(min(ans))


# t = int(input())

# for i in range(t):
#     n = int(input())
#     nums = list(map(int,input().split()))
#     nums.sort()
#     count = []
#     y = ''
#     for x in nums:
#         if x == y:
#             count[-1][1]+=1
#         else:
#             count.append([x,1])
#             y = x

#     moves = 0
#     while len(count)>1:
#         print(count)
#         gap = count[1][0]-count[0][0]
#         b = count[1][1] 
#         moves += ((gap//5) + (gap%5)//2 + (gap%5)%2)*b
#         count= count[1:]
#         for a in range(1,len(count)):
#             count[a][0] += gap

#     print(moves)