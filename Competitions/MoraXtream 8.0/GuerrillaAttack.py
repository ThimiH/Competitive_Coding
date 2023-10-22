n,m,k = tuple(map(int,input().split()))

dist = []

spies = []

for _ in range(n):
    spies.append(tuple(map(int,input().split())))

for i in range(m):
    x,y = tuple(map(int,input().split()))
    for j in range(n):
        dist.append(tuple(i,j,(x-spies[j][0])**2+(y-spies[j][1])**2))

dist = sorted(dist, key=lambda x: x[2])

print(dist)