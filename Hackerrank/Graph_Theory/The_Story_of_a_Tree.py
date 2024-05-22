from collections import deque
from math import gcd

class Tree_Node:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def find_parent(self):
        if self.parent is None:
            return self
        return self.parent.find_parent()
    
    def set_parent(self, parent):
        self.parent = parent

for test in range(int(input())):

    n = int(input())

    edges = [[] for i in range(n+1)]

    for i in range(n-1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    q, k = map(int, input().split())

    pairs = set()

    for i in range(q):
        u, v = map(int, input().split())
        pairs.add((u, v))

    tree = [Tree_Node(i) for i in range(n+1)]

    correct_pairs = [0 for i in range(n+1)]

    queue = deque([1])

    while queue:
        # print(queue)
        node = queue.popleft()
        for child in edges[node]:
            if tree[child].parent is None:
                tree[child].set_parent(tree[node])
                if (node, child) in pairs:
                    correct_pairs[1] += 1
                queue.append(child)
    # print(correct_pairs)

    queue = [1]
    visited = [False for i in range(n+1)]
    visited[1] = True
    prev_node = 1

    # add connected nodes to the queueueue
    for child in edges[1]:
        queue.append(child)

    while queue:
        node = queue[-1]
        # print(queue)
        if visited[node]:
            queue.pop()
            prev_node = tree[node].parent.name
        else:
            visited[node] = True
            # print(prev_node, node, pairs)
            if (prev_node, node) in pairs:
                correct_pairs[node] = correct_pairs[prev_node] - 1
            elif (node, prev_node) in pairs:
                correct_pairs[node] = correct_pairs[prev_node] + 1
            else:
                correct_pairs[node] = correct_pairs[prev_node]
            # print(correct_pairs)
            prev_node = node
        for child in edges[node]:
            if not visited[child]:
                queue.append(child)

    # print(k , correct_pairs)
    # print(k)

    count = 0

    for i in range(1, n+1):
        if correct_pairs[i] >= k:
            count += 1
        
    print(count//gcd(count, n), end='')
    print('/', end='')
    print(n//gcd(count, n))
            
            





    
















