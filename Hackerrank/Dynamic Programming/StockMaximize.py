for test in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    totalprofit = 0
    local_max = 0
    for num in arr[::-1]:
        if num>local_max:
            local_max = num
        else:
            totalprofit += local_max-num

    print(totalprofit)
