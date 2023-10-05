def prod(numSet):
    prod = 1
    for i in numSet:
        prod *= i
    return prod

T = int(input())
Nlist=[]
Klist=[]
intlst=[]

if 1<=T<=100:
    for x in range(T):
        inp = list(map(int,input().split()))
        if 1<=inp[1]<=13 and inp[1]<=inp[0]<=1000:
            Nlist.append(inp[0])
            Klist.append(inp[1])
            intlst.append(list(int(x) for x in str(input())))
        else:
            break

if len(Nlist)==T:
    for i in range(T):
        lrgprod = 0
        for y in range(Nlist[i]-Klist[i]+1):
            prd = prod(intlst[i][y:y+Klist[i]])
            if prd > lrgprod:
                lrgprod = prd

        print(lrgprod)