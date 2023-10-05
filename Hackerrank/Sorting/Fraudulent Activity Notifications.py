#Tuple input
n,d = tuple(map(int,input().split()))

#List input
inplst = list(map(int,input().split()))

pack = inplst[:d]
pack.sort()

count = 0

def median(lst):
    global d
    if d%2 == 0:
        return (lst[d//2-1]+lst[d//2])/2
    else:
        return lst[int((d-1)//2)]

if 2*median(pack)<=inplst[d]:
    count += 1
for ind in range(d+1,n):
    pack.remove(inplst[ind-d-1])
    pack.append(inplst[ind-1])
    pack.sort()
    if 2*median(pack)<=inplst[ind]:
        count += 1

print(count)