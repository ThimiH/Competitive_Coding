def DSU(array):
    union = []
    for pair in array:
        a = pair[0]
        b = pair[1]
        index_a = (-1)
        index_b = (-1)
        union_size = len(union)
        for index in range(union_size):
            if a in union[index]:
                index_a = index
            if b in union[index]:
                index_b = index
            if index_a!=(-1) and index_b!=(-1):
                break
        if index_a==(-1) and index_b==(-1):
            union.append(pair)
        elif index_a==(-1):
            union[index_b].append(a)
        elif index_b==(-1):
            union[index_a].append(b)
        else:
            if index_a == index_b:
                pass
            else:
                union[index_a] = union[index_a]+union[index_b]
                union.pop(index_b)
    return union

t = int(input()) 

for test in range(t):
    pair_set1 = []
    pair_set2 = []
    n,m = tuple(map(int,input().split()))
    first_queue = list(map(int,input().split()))
    second_queue = list(map(int,input().split()))
    for x in range(m):
        pair_set1.append(list(map(int,input().split())))
    for y in range(n):
        if first_queue[y]!=second_queue[y]:
            pair_set2.append([y+1,first_queue.index(second_queue[y])+1])
    
    union1 = []
    for lst in DSU(pair_set1):
        union1.append(set(lst))
    union2 = []
    for lst in DSU(pair_set2):
        union2.append(set(lst))

    status = True
    
    for bset in union2:
        if not status:
            break
        key = False
        for aset in union1:
            if bset.issubset(aset):
                key = True
                break
        if not key:
            status = False
            break
    
    if status:
        print("YES")
    else:
        print("NO")
