h,w = tuple(map(int,input().split()))
values = []
for _ in range(h):
    values+=list(map(int,input().split()))
print(max(values))