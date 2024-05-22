from collections import defaultdict
import heapq

n,m = map(int,input().strip().split())

paths = defaultdict(list)

for i in range(m):
    a,b,w = map(int,input().strip().split())
    paths[a].append((b,w))
    paths[b].append((a,w))

def search(start,end):
    visited = [False]*(n+1)
    visited[start] = True
    heap = [(0,start)]
    while heap:
        w,v = heapq.heappop(heap)
        if v == end:
            return w
        else:
            visited[v] = True
        for u,weight in paths[v]:
            if not visited[u]:
                heapq.heappush(heap,(max(w,weight),u))
    return "NO PATH EXISTS"

print(search(1,n))