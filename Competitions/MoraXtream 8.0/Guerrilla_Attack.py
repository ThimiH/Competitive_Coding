from collections import defaultdict

n,m,k = tuple(map(int,input().split()))

dist = []
spies = []

for _ in range(n):
    spies.append(tuple(map(int,input().split())))

for i in range(m):
    x,y = tuple(map(int,input().split()))
    for j in range(n):
        dist.append((j,i+n,(x-spies[j][0])**2+(y-spies[j][1])**2))

dist = sorted(dist, key=lambda x: x[2])

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph

    def bfs(self, source, target, parent):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for ind, capacity in enumerate(self.graph[u]):
                if not visited[ind] and capacity > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[target]

    def max_flow(self, source, target):
        parent = [-1] * len(self.graph)
        max_flow = 0

        while self.bfs(source, target, parent):
            path_flow = float('inf')
            s = target

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = target

            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

source = n+m
sink = n+m+1

dummy = [[0]*(n+m+2) for _ in range(n+m+2)]

for i in range(n):
    dummy[source][i] = 1

for i in range(n,n+m):
    dummy[i][sink] = 1

left = 0
right = n*m-1
ans = -1

while left <= right:
    mid = left + (right - left) // 2  # Calculate the middle index
    graph = [[0]*(n+m+2) for _ in range(n+m+2)]

    for i in range(n):
        graph[source][i] = 1

    for i in range(n,n+m):
        graph[i][sink] = 1

    for i in range(mid):
        edge = dist[i]
        graph[edge[0]][edge[1]] = 1
    ff = FordFulkerson(graph)
    max_flow = ff.max_flow(source, sink)

    if max_flow == k:
        ans = mid
        right = mid - 1
    elif max_flow < k:
        left = mid + 1
    else:
        right = mid - 1

print(dist[ans-1][2])