import numpy as np

n = int(input())
dim = 2*(n+2)-1
k=n+1

arr = np.empty((dim,dim),dtype='<U2')
arr
zs = '00'

for i in range(n+2):
    if i<9 :
        arr[0:dim,k-i] = (' '+str(i+1))
        arr[0:dim,k+i] = (' '+str(i+1))
        arr[k-i,0:dim] = (' '+str(i+1))
        arr[k+i,0:dim] = (' '+str(i+1))
        print(' '+str(i+1))

    else :
        arr[0:dim,k-i] = str(i+1)
        arr[0:dim,k+i] = str(i+1)
        arr[k-i,0:dim] = str(i+1)
        arr[k+i,0:dim] = str(i+1)
    
arr[0:2,0:dim] = zs
arr[dim-2:dim,0:dim] = zs

y=n-2
x=5

for i in range(n-3):
    arr[y,0:x] = zs
    arr[y,dim-x:dim] = zs
    y -= 1
    x += 1

y=n
x=1

for i in range(n+1):
    arr[y,0:x] = zs
    arr[y,dim-x:dim] = zs
    y += 1
    x += 1

for i in range(dim):
    row = ' '.join(item for item in arr[i,0:dim])
    print(row)