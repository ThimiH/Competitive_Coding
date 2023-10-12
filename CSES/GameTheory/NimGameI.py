for test in range(int(input())):
    n = int(input())
    x_array = list(map(int,input().split()))

    factor = 0
    for num in x_array:
        factor ^= num
    
    if factor:
        print('first')
    else:
        print('second')