n,m = tuple(map(int,input().split()))

grid = []
for i in range(m):
    grid.append(list(map(int,input().split())))

A = list(map(int,input().split()))

consrv = 5
odd = A[0]
try:
    ev = A[1]
except:
    ev = 0
dif = (max(odd,ev)-min(odd,ev))

check = 1

for item in A:
    if item!=odd and item!=ev:
        check = 0

ans = -1

if check == 1:
    for i in range(1,consrv):
        nb = m - odd//i
        nc = m - ev//i
        na = m - (nb+nc)
        if na>=0 and nb>=0 and nc>=0 and (na+nb)*i == ev and (na+nc)*i == odd:
            ans = 'a'*na + 'b'*nb + 'c'*nc
            break

print(ans)