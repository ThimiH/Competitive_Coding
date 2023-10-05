import math

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, start):
        # Initialize distances
        distances = [float("inf")] * self.V
        distances[start] = 0
        # Relax edges repeatedly
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distances[u] != float("inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
        return distances

n,m = tuple(map(int,input().split()))

grid = Graph(n)

for _ in range(m):
    u,v,w = tuple(map(int,input().split()))
    grid.add_edge(v-1,u-1,w)

d,q = tuple(map(int,input().split()))

friends = list(map(int,input().split()))

result = grid.bellman_ford(d-1)

for friend in friends:
    if not math.isinf(result[friend-1]):
        print(result[friend-1])
    else:
        print("Impossible")