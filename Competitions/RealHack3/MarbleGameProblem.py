n = int(input())
inplst = sorted(list(map(int,input().split())))

ans = 0

for val in inplst:
    ans *= 2
    ans += val

print(ans)