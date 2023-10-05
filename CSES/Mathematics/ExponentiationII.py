for test in range(int(input())):
    a,b,c = tuple(map(int,input().split()))
    if b == 0:
        if c == 0:
            print(a)
        else:
            print(1)
    else:
        print(pow(a,pow(b,c,10**9+6),10**9+7))