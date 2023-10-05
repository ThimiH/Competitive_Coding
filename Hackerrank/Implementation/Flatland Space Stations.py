#Tuple input
n,m = tuple(map(int,input().split()))

#List input
spacelst = list(map(int,input().split()))
spacelst.sort()


ans = 0

a = spacelst[0]-0
if a>ans:
    ans = a

b = n-1-spacelst[-1]
if b>ans:
    ans = b

for ind in range(1,m):
    c = (spacelst[ind]-spacelst[ind-1])//2
    if c > ans:
        ans = c

print(ans)