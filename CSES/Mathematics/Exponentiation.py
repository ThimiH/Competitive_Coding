for test in range(int(input())):
    a,b = tuple(map(int,input().split()))
    print(pow(a,b,10**9+7))