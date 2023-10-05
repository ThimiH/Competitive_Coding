n,p = tuple(map(int,input().split()))

docdict = dict()

for i in range(n):
    docdict[i]=[]

for i in range(p):
    d1,d2 = tuple(map(int,input().split()))
    docdict[d1].append(d2)
    docdict[d2].append(d1)

cdct = dict()
cnum = 0

while len(docdict.keys())>0:
    lst = docdict(list(docdict.keys())[0])
    docdict.pop(list(docdict.keys())[0])
    cdct[cnum] = lst
    while len(lst)>0:
        if lst[0] in list(docdict.keys())[0]:
            newlst = docdict(lst[0])
            docdict.pop(lst[0])
            lst = lst[1:]
            cdct[cnum].append(newlst)
            for x in newlst:
                if x in docdict.keys():
                    lst.append(x)
    cnum+=1

countlst = []
for a in cdct.keys():
    countlst.append(len(set(cdct[a])))

ans = 0
nn = n

for num in countlst:
    nn-=num
    ans+=num*nn

print(ans)