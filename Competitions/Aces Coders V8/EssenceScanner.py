#Wrong

N,M = tuple(map(float,input().split()))

total_xm = 0
total_ym = 0
total_mass = 0

for _ in range(N):
    x,y,m = tuple(map(float,input().split()))
    total_xm += x*m
    total_ym += y*m
    total_mass += m

print(round(total_xm/total_mass),round(total_ym/total_mass))
print(round(total_xm/(total_mass+M)),round(total_ym/(total_mass+M)))