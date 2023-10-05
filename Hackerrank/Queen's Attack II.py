n,o = tuple(map(int,input().split()))
posq = tuple(map(int,input().split()))

def go(pos,dir):
    hi = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    return tuple([pos[0]+hi[dir][0],pos[1]+hi[dir][1]])

obslst = []

for q in range(o):
    new = tuple(map(int,input().split()))
    if new[0]==posq[0] or new[1]==posq[1] or new[0]-posq[0]==new[1]-posq[1] or new[0]-posq[0]==-(new[1]-posq[1]):
        obslst.append(new)

ans = 0

for i in range(8):
    pos = go(posq,i)
    while 1<=pos[0]<=n and 1<=pos[1]<=n:
        if pos in obslst:
            break
        else:
            ans+=1
            pos = go(pos,i)

print(ans)