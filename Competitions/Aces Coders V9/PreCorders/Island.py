y=int(input())
x=int(input())

land=[]
indexes = []
area = [0]

if 0<x<10 and 0<y<10:
    for n in range(y):
        land.append(list(map(int, input().split())))
        
    for m in range(x):
        for n in range(y):
            if land[n][m]==1:
                indexes.append([m,n])

def AOE1(ind):
    global indexes
    global area
    area[-1]+=1

    AOE = []
    if [ind[0]+1,ind[1]] in indexes:
        area[-1]+=1
        AOE.append([ind[0]+1,ind[1]])
        indexes.remove([ind[0]+1,ind[1]])
    
    if [ind[0]-1,ind[1]] in indexes:
        area[-1]+=1
        AOE.append([ind[0]-1,ind[1]])
        indexes.remove([ind[0]-1,ind[1]])

    if [ind[0],ind[1]+1] in indexes:
        area[-1]+=1
        AOE.append([ind[0],ind[1]+1])
        indexes.remove([ind[0],ind[1]+1])

    if [ind[0],ind[1]-1] in indexes:
        area[-1]+=1
        AOE.append([ind[0],ind[1]-1])
        indexes.remove([ind[0],ind[1]-1])

    if [ind[0]+1,ind[1]+1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]+1,ind[1]+1])
        indexes.remove([ind[0]+1,ind[1]+1])

    if [ind[0]+1,ind[1]-1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]+1,ind[1]-1])
        indexes.remove([ind[0]+1,ind[1]-1])

    if [ind[0]-1,ind[1]+1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]-1,ind[1]+1])
        indexes.remove([ind[0]-1,ind[1]+1])

    if [ind[0]-1,ind[1]-1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]-1,ind[1]-1])
        indexes.remove([ind[0]-1,ind[1]-1])

    for k in AOE:
        AOE2(k)
    
    area.append(0)

def AOE2(ind):
    global indexes
    global area

    AOE = []
    if [ind[0]+1,ind[1]] in indexes:
        area[-1]+=1
        AOE.append([ind[0]+1,ind[1]])
        indexes.remove([ind[0]+1,ind[1]])
    
    if [ind[0]-1,ind[1]] in indexes:
        area[-1]+=1
        AOE.append([ind[0]-1,ind[1]])
        indexes.remove([ind[0]-1,ind[1]])

    if [ind[0],ind[1]+1] in indexes:
        area[-1]+=1
        AOE.append([ind[0],ind[1]+1])
        indexes.remove([ind[0],ind[1]+1])

    if [ind[0],ind[1]-1] in indexes:
        area[-1]+=1
        AOE.append([ind[0],ind[1]-1])
        indexes.remove([ind[0],ind[1]-1])

    if [ind[0]+1,ind[1]+1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]+1,ind[1]+1])
        indexes.remove([ind[0]+1,ind[1]+1])

    if [ind[0]+1,ind[1]-1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]+1,ind[1]-1])
        indexes.remove([ind[0]+1,ind[1]-1])

    if [ind[0]-1,ind[1]+1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]-1,ind[1]+1])
        indexes.remove([ind[0]-1,ind[1]+1])

    if [ind[0]-1,ind[1]-1] in indexes:
        area[-1]+=1
        AOE.append([ind[0]-1,ind[1]-1])
        indexes.remove([ind[0]-1,ind[1]-1])

    for k in AOE:
        AOE2(k)
    
while True:
    if len(indexes)==0:
        break

    iterest = indexes[0]
    indexes.remove(iterest)
    AOE1(iterest)

if 0<x<10 and 0<y<10:
    print(max(area))          
