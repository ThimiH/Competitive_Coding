def Status(n):
    val = [True for i in range(n+1)]
    val[0] = val[1] = False
    for ind in range(2,int(n**0.5)+1):
        if val[ind]:
            for x in range(ind**2,n+1,ind):
                val[x]=False
    for x in range(1,n):
        if x**2> n:
            break
        val[x**2]=True
    return val

m,n = tuple(map(int,input().split()))

Condition = Status(n)

ans = 0

for ind in range(m,n+1):
    if not Condition[ind]:
        ans += 1

print(ans)