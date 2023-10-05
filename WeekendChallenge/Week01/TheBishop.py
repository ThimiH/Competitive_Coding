coords = list(map(int,input().split()))

if (coords[0]+coords[1])%2 == (coords[2]+coords[3])%2:
    if (coords[0]==coords[2]) and (coords[1]==coords[3]):
        print(0)
    elif (coords[0]-coords[2]) == (coords[1]-coords[3]):
        print(1)
    else:
        print(2)
else:
    print(-1)