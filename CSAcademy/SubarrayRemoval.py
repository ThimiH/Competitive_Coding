#Wrong

n = int(input())
values = list(map(int,input().split()))

ending = [0]*n
ending[0] = values[0]
starting = [0]*n
starting[-1] = values[-1]

for i in range(1,n):
    ending[i] = ending[i-1]+values[i]
    starting[n-1-i] = starting[n-i]+values[n-1-i]

ans = 0

for i in range(n):
    for j in range(i,n):
        if i == 0:
            if j != n-1:
                ans = max(ans,starting[j+1])
        elif j == n-1:
            if i != 0:
                ans = max(ans,ending[i-1])
        else:
            ans = max(ans,ending[i-1]+starting[j+1])

print(ans)