n,p = tuple(map(int,input().split()))

#Sieve of Eratosthenes
def SOE(n,p):
    primes = []
    val = [True for i in range(n+1)]
    val[0] = val[1] = False
    for ind in range(2,p):
        if val[ind]:
            for x in range(ind**2,n+1,ind):
                val[x]=False
    for y in range(p+1,n+1):
        if val[y]:
            primes.append(y)
    return primes

primes = SOE(max(p,int(10**9//p)),p)

print(len(primes),primes[0])