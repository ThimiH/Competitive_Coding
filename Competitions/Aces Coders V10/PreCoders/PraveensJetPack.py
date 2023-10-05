tests = []
max_n = 0
for i in range(int(input())):
    n=int(input())
    max_n = max(max_n,n)
    tests.append(n)

grid = [1]*(max_n+1)
mod = 10**9+7
for i in range(1,max_n+1):
    grid[i]=(grid[i-1]*((2*i-1)%mod)*((2*i)%mod)*pow(i,mod-2,mod)*pow(i+1,mod-2,mod))%mod

for test in tests:
    print(grid[test])

# tests = []
# max_n = 0
# for i in range(int(input())):
#     n=int(input())
#     max_n = max(max_n,n)
#     tests.append(n)

# grid = [1]*(n+1)
# mod = 10**9+7
# for i in range(2,n+1):
#     grid[i]=(grid[i-1]*(4*i**2-2*i)//(i**2+i))%mod

# for test in tests:
#     print(grid[test])