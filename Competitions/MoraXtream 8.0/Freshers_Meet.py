n,m = tuple(map(int,input().split()))
hs = list(map(int,input().split()))

for round in range(m):
    l,r,x = tuple(map(int,input().split()))
    ans = -1
    tot = hs[l-1]
    p1 = l-1
    p2 = l-1
    while p2<r:
        power = tot*2*(p2-p1+1)
        if power>=x:
            if ans != -1:
                ans = min(ans,max(hs[p1:p2+1]))
            else:
                ans = max(hs[p1:p2+1])
            if p1==p2:
                p2+=1
                if p2!=r:
                    tot+=hs[p2]
            tot-=hs[p1]
            p1+=1 
        else:
            p2+= 1
            if p2!=r:
                    tot+=hs[p2]
    p2-=1
    while p1<r:
        power = tot*2*(p2-p1+1)
        if power>=x:
            if ans != -1:
                ans = min(ans,max(hs[p1:p2+1]))
            else:
                ans = max(hs[p1:p2+1])
        
        tot-=hs[p1]
        p1+=1

    
    print(ans)
