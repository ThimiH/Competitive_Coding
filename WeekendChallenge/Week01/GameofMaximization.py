n = int(input())
stones = list(map(int,input().split()))

totals = [0,0]
ind = True

for pile in stones:
    if ind:
        totals[0]+=pile
        ind = False
    else:
        totals[1]+=pile
        ind = True

print(2*min(totals))
