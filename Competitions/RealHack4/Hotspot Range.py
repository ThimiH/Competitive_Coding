#Tuple input
n,k = tuple(map(int,input().split()))

#List input
inpst = set(map(int,input().split()))

inplst = list(inpst)
inplst.sort()

l = len(inplst)
ind = 0
hp = 0

a = inplst[ind]
b = inplst[ind]

while ind<l:
    hp+=1
    while (b-a)<=k:
        ind += 1
        try:
            b = inplst[ind]
        except:
            break
    a = inplst[ind-1]
    while (b-a)<=k:
        ind += 1
        try:
            b = inplst[ind]
        except:
            break
    a = b

print(hp)
