n,k = tuple(map(int,input().split()))

exp = 0

for i in range(1,k+1):
    exp += (pow(i/k,n)-pow((i-1)/k,n))*i

print("%.6f" %exp)