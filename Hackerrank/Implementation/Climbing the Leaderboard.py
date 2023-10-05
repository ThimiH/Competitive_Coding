n1 = int(input())
ranked = list(set(map(int,input().split())))
n2 = int(input())
player = list(map(int,input().split()))

ranked.sort()

l=len(ranked)
rind = 0
pind = 0
place = l+1

for item in player:
    if rind<l:
        if ranked[rind]>item:
            print(place)
        else:
            if rind<l:
                while ranked[rind]<=item:
                    rind += 1
                    place -= 1
                    if rind==l:
                        break
            try:
                print(place)
            except:
                print(1)
    else:
        print(1)