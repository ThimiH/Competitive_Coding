for test in range(int(input())):
    n = int(input())
    x_array = list(map(int,input().split()))

    factor = 0
    for ind,num in enumerate(x_array):
        if ind%2:
            factor ^= num
    
    if factor:
        print('first')
    else:
        print('second')