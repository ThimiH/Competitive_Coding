for test in range(int(input())):
    i,c = tuple(map(int,input().split()))
    status = "NO"
    connections = {}
    for point in range(1,i+1):
        connections[point]=[]
    for _ in range(c):
        a,b = tuple(map(int,input().split()))
        connections[min(a,b)].append(max(a,b))
    digital = [False for _ in range(i+1)]
    visited = [False for _ in range(i+1)]
    visited[1] = True
    for point in range(1,i+1):
        if not visited[point]:
            pass
        else:
            for next_point in connections[point]:
                if visited[next_point] and digital[point]!=digital[next_point]:
                    pass
                else:
                    if visited[next_point]:
                        status="YES"
                        break
                    else:
                        visited[next_point]=True
                        digital[next_point]= not digital[point]
            if status=="YES":
                break
    print(status)