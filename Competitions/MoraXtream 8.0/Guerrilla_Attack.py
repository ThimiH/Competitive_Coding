n,m,k = tuple(map(int,input().split()))

dist = []

spies = []

for _ in range(n):
    spies.append(tuple(map(int,input().split())))

for i in range(m):
    x,y = tuple(map(int,input().split()))
    for j in range(n):
        dist.append((i,j,(x-spies[j][0])**2+(y-spies[j][1])**2))

dist = sorted(dist, key=lambda x: -x[2])

m_count = [n]*m
n_count = [m]*n
m_avl = m-k
n_avl = n-k

def checker(i,j):
    global m_count,n_count,n_avl,m_avl
    if m_count[i]==1 and m_avl==0:
        return False
    if n_count[j]==1 and n_avl==0:
        return False
    return True

for tup in dist:
    i,j,d = tup
    if checker(i,j):
        m_count[i]-=1
        n_count[j]-=1
        if m_count[i] == 0:
            print(i)
            m_avl-=1
        if n_count[j] == 0:
            print("j",j)
            n_avl-=1
        print(tup,m_count,m_avl,n_count,n_avl)
    else:
        print('else')
        print(tup,m_count,m_avl,n_count,n_avl)
        print(d)
        break
