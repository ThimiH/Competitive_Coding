#Sieve of Eratosthenes - Use python 3
def SOE(n):
    val = [True for i in range(n+1)]
    val[0] = val[1] = False
    for ind in range(2,int(n**0.5)+1):
        if val[ind]:
            for x in range(ind**2,n+1,ind):
                val[x]=False
    return val

LIMIT = 10**6
primes = SOE(LIMIT)

t = int(input())

for test_case in range(t):
    down,up = 0,0
    a,b = tuple(map(int,input().split()))
    for index in range(a,b+1):
        if primes[index]:
            down = index
            break
    for index in range(b,a-1,-1):
        if primes[index]:
            up = index
            break
    print(up-down)
    