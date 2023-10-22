N,M = tuple(map(int,input().split()))

platforms = []

for platfom in range(N):
    platforms.append(tuple(map(int,input().split())))

balls = sorted(list(map(int,input().split())))

gaps = [float('INF')]

for i in range(M):
    gaps.append(balls[i+1]-balls[i]-1)

gaps.append(float('INF'))

