n,k = tuple(map(int,input().split()))
inplst = list(map(int,input().split()))

height = 0

for i in range(n):
    if inplst[i]>height:
        height = inplst[i]

print(max(0,height-k))