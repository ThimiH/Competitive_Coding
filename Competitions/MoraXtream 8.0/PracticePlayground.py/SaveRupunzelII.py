for _ in range(int(input())):
    n = int(input())
    values = sorted(list(map(int,input().split())))
    ans = [-1]*n
    js = list(range(n-1,-1,-1))
    remain = n
    for i in range(n-1,-1,-1):
        for ind in range(n):
            if i == j:
                pass
            elif values[i]<=values[j]*2:
                ans[j] = values[i]
                
            else:
                break

                

