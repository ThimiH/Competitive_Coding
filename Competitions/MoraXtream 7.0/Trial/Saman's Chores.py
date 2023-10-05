K,L = tuple(map(int,input().split()))
plan = {}

if 1<=K<=1000 and 0<=L<=1000000:
    for i in range(L):
        a,b = tuple(map(int,input().split()))
        try:
            plan[a].append(b)
        except:
            plan[a]=[b]

    order = list(map(int,input().split()))

    if 1<=min(order) and max(order)<=K:
        keylst = plan.keys()
        out = "YES"
        for item in keylst:
            for event in plan[item]:
                if event not in order[order.index(item):]:
                    out = 'NO'
                    break
            if out == 'NO':
                break
        
        print(out)