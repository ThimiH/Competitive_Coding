# Half Done

n = int(input())
lst = list(map(int,input().split()))

xor = 0

for num in lst:
    xor ^= num

if xor == 0:
    print(0)
else:
    print(-1)