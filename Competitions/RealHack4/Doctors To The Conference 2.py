n,p = tuple(map(int,input().split()))

docset = []

ab = ['a','b']

for i in range(n):
    docset.append([i])

for i in range(p):
    d1,d2 = tuple(map(int,input().split()))
    k=0
    for i in range(len(docset)):
        if d1 in docset[i] or d2 in docset[i]:
            ab[k]=i
            k+=1
        if k == 2:
            break
    if ab[0]!=ab[1]:
        docset.append(docset[ab[0]]+docset[ab[1]])
        docset.pop(max(ab[0],ab[1]))
        docset.pop(min(ab[0],ab[1]))

ans=0

for lst in docset:
    l=len(lst)
    n-=l
    ans+=l*n

print(ans)