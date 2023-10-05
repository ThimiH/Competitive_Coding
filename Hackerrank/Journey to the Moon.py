n,p = tuple(map(int,input().split()))
Ndict = {}
ccount = []

for i in range(n):
    Ndict[i]=[]

for pair in range(p):
    two = list(map(int,input().split()))
    Ndict[two[0]].append(two[1])
    Ndict[two[1]].append(two[0])
    Ndict[two[0]].sort()
    Ndict[two[1]].sort()

names = list(range(n))

while len(names)>0:
    ccount.append(1)
    name = names[0]
    names = names[1:]
    nameq = []
    nameq += Ndict[name]
    ccount[-1] += len(Ndict[name])
    for one in nameq:
        names.remove(one)
    while len(nameq)>0:
        name = nameq[0]
        nameq = nameq[1:]
        current = Ndict[name]
        avl = []
        for one in current:
            if one in names:
                avl.append(one)
                names.remove(one)
        nameq += avl
        ccount[-1] += len(avl)

comb = 0
cnt = 0

for i in range(len(ccount)):
    val = ccount[i]
    cnt += val
    comb += val*(n-cnt)

print(comb)