n = int(input())

arr = list(map(int,input().split()))

ans = []

for i in range(n):
    ans.append(str(arr[i-1]+arr[(i+1)%n]))

print(' '.join(ans))