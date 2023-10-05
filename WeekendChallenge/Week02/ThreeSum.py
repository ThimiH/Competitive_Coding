n,m = tuple(map(int,input().split()))

ans = 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a+b>=m :
            break
        else:
            if m-(a+b)<=n:
                ans += 1

print(ans)