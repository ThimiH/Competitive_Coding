n = int(input())
counts = list(map(int,input().split()))
locations = list(map(int,input().split()))
covered = [[]]*n

m = int(input())
fun_locations = list(map(int,input().split()))
fun_radius = list(map(int,input().split()))
single_count = [0]*m

for i in range(m):
    s = fun_locations[i]-fun_radius[i]
    e = fun_locations[i]+fun_radius[i]

    for j in range(n):
        if s<=locations[j] and locations[j]<=e:
            covered[j].append(i)

ans = 0

for j in range(n):
    if len(covered[j])==0:
        ans+=covered
    elif len(covered[j])==1:
        single_count[covered[j][0]]+=counts[j]

ans += max(single_count)

print(ans)