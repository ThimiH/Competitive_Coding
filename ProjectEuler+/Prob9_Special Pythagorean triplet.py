def pyfind(num):
    out = [-1]
    for a in range(1,num):
        for b in range(a,num):
            c = num -a -b
            if c**2 == a**2 + b**2:
                out.append(a*b*c)
            if b>a+c:
                break
    return out

T = int(input())
Nlist=[]
Anslist=[]

if 1<=T<=3000:
    for y in range(T):
        N = int(input())
        if 1<=N<=3000:
            if N in Nlist:
                Anslist.append(Anslist[Nlist.index(N)])
            else:
                Anslist.append(max(pyfind(N)))
            Nlist.append(N)

if len(Anslist)==T:
    for val in Anslist:
        print(val)