for _ in range(int(input())):
    a,b = tuple(map(int,input().split()))
    c = 2*min(a,b)-max(a,b)
    if c<0 or c%3!=0:
        print('NO')
    else:
        print('YES')