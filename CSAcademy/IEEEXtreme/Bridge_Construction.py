from collections import defaultdict

def find_longest_path(tree, start):
    def dfs(node, parent, distance, current_path):
        nonlocal max_distance, farthest_node, longest_path
        if distance > max_distance:
            max_distance = distance
            farthest_node = node
            longest_path = current_path.copy()

        for neighbor in tree[node]:
            if neighbor != parent:
                current_path.append(neighbor)
                dfs(neighbor, node, distance + 1, current_path)
                current_path.pop()

    max_distance = -1
    farthest_node = -1
    longest_path = []

    # Find the farthest node from the start
    dfs(start, -1, 0, [start])

    # Find the farthest node from the farthest node found in the previous step
    dfs(farthest_node, -1, 0, [farthest_node])

    return max_distance, longest_path

for test in range(int(input())):
    
    n = int(input())
    tree_1 = {i:[] for i in range(1,n+1)}
    for _ in range(n-1):
        a,b = tuple(map(int,input().split()))
        tree_1[a].append(b)
        tree_1[b].append(a)
    
    m = int(input())
    tree_2 = {i:[] for i in range(1,m+1)}
    for _ in range(m-1):
        a,b = tuple(map(int,input().split()))
        tree_2[a].append(b)
        tree_2[b].append(a)

    max_distance_1, longest_path_1 = find_longest_path(tree_1,1)
    max_distance_2, longest_path_2 = find_longest_path(tree_2,1)
    # print(max_distance_1, longest_path_1, max_distance_2, longest_path_2)
    print((max_distance_1+1)//2+(max_distance_2+1)//2+1)
    print(longest_path_1[max_distance_1//2],longest_path_2[max_distance_2//2])



# # Example usage:
# tree = {
#     0: [1, 2],
#     1: [0, 3, 4],
#     2: [0],
#     3: [1],
#     4: [1]
# }
# start_node = 0
# max_distance, longest_path = find_longest_path(tree, start_node)
# print("Longest path length:", max_distance)
# print("Longest path:", longest_path)
