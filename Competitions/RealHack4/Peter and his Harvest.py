#Tuple input
n,m = tuple(map(int,input().split()))

#List input
A = list(map(int,input().split()))
B = list(map(int,input().split()))
AB =  [A[k]*B[k] for k in range(n)]
for days in range(m):
    ind = AB.index(max(AB))
    A[ind]-=1
    AB[ind]-=B[ind]

print(A.join(' '))
