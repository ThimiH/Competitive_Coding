n = int(input())

costs = list(map(int,input().split()))
now = list(map(int,input().split()))
final = list(map(int,input().split()))

now_d = {}

for i in range(n):
    now_d[now[i]] = i

for i in range(n):
    now[now_d[final[i]]]=(i,costs[now_d[final[i]]])

ans = 0

for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if now[i][0]>now[j][0]:
            ans += now[i][1]+now[j][1]
            temp = now[i]
            now[j] = now[i]
            now[i] = temp
        else:
            pass

print(ans)