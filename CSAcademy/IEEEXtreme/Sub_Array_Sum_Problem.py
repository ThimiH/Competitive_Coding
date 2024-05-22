dim = int(input())
lens = list(map(int,input().split()))
elements = list(map(int,input().split()))

element_dict = dict()

def element_find(coordinate):
    global elements,dim,lens
    ind = 0
    for ind,i in enumerate(coordinate):
        ind = ind*lens[ind-1]+i-1
    print(coordinate,elements[ind])
    return elements[ind+1]

for quarry in range(int(input())):
    ans = 0
    p1 = list(map(int,input().split()))
    p2 = list(map(int,input().split()))
    if dim == 1:
        for i in range(p1[0]-1,p2[0]):
            ans += element_find([i])
    elif dim == 2:
        for i in range(p1[0]-1,p2[0]):
            for j in range(p1[1]-1,p2[1]):
                ans += element_find((i,j))
    elif dim == 3:
        for i in range(p1[0]-1,p2[0]):
            for j in range(p1[1]-1,p2[1]):
                for k in range(p1[2]-1,p2[2]):
                    ans += element_find((i,j,k))
    elif dim == 4:
        for i in range(p1[0]-1,p2[0]):
            for j in range(p1[1]-1,p2[1]):
                for k in range(p1[2]-1,p2[2]):
                    for l in range(p1[2]-1,p2[2]):
                        ans += element_find((i,j,k,l))
    else:
        for i in range(p1[0]-1,p2[0]):
            for j in range(p1[1]-1,p2[1]):
                for k in range(p1[2]-1,p2[2]):
                    for l in range(p1[2]-1,p2[2]):
                        for m in range(p1[0]-1,p2[0]):
                            ans += element_find((i,j,k,l,m))

    print(ans)
