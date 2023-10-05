from collections import deque
import bisect

def bfs_with_paths(tree):
    all_paths = {}  # To store all shortest paths between nodes

    for start_node in tree.keys():
        visited = {}  # To keep track of visited nodes
        queue = deque()  # Initialize a queue for BFS

        # Initialize the queue with the current start node and an empty path
        queue.append((start_node, []))
        visited[start_node] = True

        while queue:
            node, path = queue.popleft()  # Dequeue a node and its path

            # Store the path from the start_node to the current node
            all_paths[(start_node, node)] = path + [node]

            # Process neighbors of the current node
            for neighbor in tree[node]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    new_path = path + [node]
                    queue.append((neighbor, new_path))

    return all_paths

def insert_sorted(lst, item):
    bisect.insort_left(lst, item)

tree = {}

n = int(input())

for i in range(n):
    tree[i] = []

values = list(map(int,input().split()))

for _ in range(n-1):
    u,v = tuple(map(int,input().split()))
    tree[u].append(v)
    tree[v].append(u)

all_shortest_paths = bfs_with_paths(tree)

q = int(input())

for work in range(q):
    s,e,k = tuple(map(int,input().split()))
    path = all_shortest_paths[min(s,e),max(s,e)]
    l = len(path)
    if l<=2:
        print(0)
    else:
        path = path[1:l-1]
        costs = []
        for node in path:
            insert_sorted(costs,values[node])
            costs.append(0)
        for i in range(l-2):
            if costs[i]<=k:
                costs[i+1]+=costs[i]
            else:
                break
        print(i)
