N  = int(input())

if 4<=N<=97:
    Grid = []
    Row = []
    for i in range(2*N+3):
        Row.append('00')
    for i in range(2*N+3):
        Grid.append(Row.copy())

    mid = N+1
    correct_N = [[mid-N+2,mid-2],[mid+N-2,mid-2]]
    correctN = [[mid-N+1,mid-1],[mid+N-1,mid-1],[mid-N+1,mid-2],[mid+N-1,mid-2]]
    correctN_= [[mid-N,mid-1],[mid+N,mid-1],[mid-N,mid-2],[mid+N,mid-2]]
    correctN__ = [[mid-N-1,mid-2],[mid+N+1,mid-2]]

    for i in range(N):
        down = mid - i
        up = mid +i
        for y in range(down,up+1):
            for x in range(down,up+1):
                if (x == down or y == down or x == up or y == up) and (1<y<2*N+1) and (1<x<2*N+1) and ((y == down and mid-N+i+1<=x<=mid+N-i-1)or(y == up and mid-N+i+1<=x<=mid+N-i-1)or(x == down and mid-N+i+1<=y<=mid+N-i-1)or(x == up and mid-N+i+1<=y<=mid+N-i-1)) :
                    if i+1 <10:
                        Grid[y][x]=(' '+str(i+1))
                    else :
                        Grid[y][x]= str(i+1)
    
    for [x,y] in correct_N:
        if N-1 <10:
            Grid[y][x]=(' '+str(N-1))
        else :
            Grid[y][x]= str(N-1)
    for [x,y] in correctN:
        if N <10:
            Grid[y][x]=(' '+str(N))
        else :
            Grid[y][x]= str(N)
    for [x,y] in correctN_:
        if N+1 <10:
            Grid[y][x]=(' '+str(N+1))
        else :
            Grid[y][x]= str(N+1)
    for [x,y] in correctN__:
        if N+2 <10:
            Grid[y][x]=(' '+str(N+2))
        else :
            Grid[y][x]= str(N+2)

    for lin in Grid:
        print(' '.join(lin))



'''
n = int(input())
dim = 2*(n+2)-1
k=n+1
rlst = []
arr = []

for i in range(dim):
    rlst.append(' ')
    
for i in range(dim):
    arr.append(rlst)
    

#arr = list((dim,dim),dtype='<U2')
arr
zs = '00'

for i in range(n+2):
    if i<9 :
        arr[0:dim][k-i] = ' '+str(i+1)
        arr[0:dim][k+i] = ' '+str(i+1)
        arr[k-i][0:dim] = ' '+str(i+1)
        arr[k+i][0:dim] = ' '+str(i+1)

    else :
        arr[0:dim][k-i] = str(i+1)
        arr[0:dim][k+i] = str(i+1)
        arr[k-i][0:dim] = str(i+1)
        arr[k+i][0:dim] = str(i+1)
    
arr[0:2][0:dim] = zs
arr[dim-2:dim][0:dim] = zs

y=n-2
x=5

for i in range(n-3):
    arr[y][0:x] = zs
    arr[y][dim-x:dim] = zs
    y -= 1
    x += 1

y=n
x=1

for i in range(n+1):
    arr[y][0:x] = zs
    arr[y][dim-x:dim] = zs
    y += 1
    x += 1

print(arr)
for i in range(dim):
    row = ' '.join(item for item in arr[i][0:dim])
    print(row)

'''