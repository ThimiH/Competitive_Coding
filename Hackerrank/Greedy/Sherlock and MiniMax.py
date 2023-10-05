n = int(input()) 

inplst = list(map(int,input().split()))
inplst.sort()

p,q = tuple(map(int,input().split()))

valdict ={}

if inplst[0]>=p:
    valdict[p]=inplst[0]-p

if inplst[-1]<=q:
    valdict[q]=q-inplst[-1]

for ind in range(n-1):
    a,b = inplst[ind],inplst[ind+1]
    val = (b-a)//2
    if p<=val<=q:
        valdict[val] = val - a
    if a<=p<=b:
        valdict[p] = min(p-a,b-p)
    if a<=q<=b:
        valdict[q] = min(q-a,b-q)

ans = -1
currmax = -1

ky = list(valdict.keys())
ky.sort()

for x in ky:
    if valdict[x]>currmax:
        currmax = valdict[x]
        ans = x

print(ans)
#!!!Wrong