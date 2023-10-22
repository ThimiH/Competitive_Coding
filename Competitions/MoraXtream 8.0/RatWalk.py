def has_path_dfs(matrix, start, target, visited=None):
    if visited is None:
        visited = set()

    if start == target:
        return True

    visited.add(start)

    for i in range(len(matrix[start])):
        if matrix[start][i] == 1 and i not in visited:
            if has_path_dfs(matrix, i, target, visited):
                return True

    return False

t,w,h=tuple(map(int,input().split()))

for test  in range(t):
    n,r = tuple(map(int,input().split()))
    x_s = list(map(int,input().split()))
    y_s = list(map(int,input().split()))
    graph = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n):
        x_1,y_1 = x_s[i],y_s[i]
        if x_1 <= r:
            graph[i][n] = graph[n][i] = 1
        if w-x_1 <= r:
            graph[i][n+1] = graph[n+1][i] = 1
        for j in range(i):
            x_2,y_2 = x_s[j],y_s[j]
            d = ((x_1-x_2)**2+(y_1-y_2)**2)**0.5
            if d<=2*r:
                graph[i][j] = graph[j][i] = 1

    if has_path_dfs(graph, n, n+1):
        print("CAN'T")
    else:
        print("CAN")