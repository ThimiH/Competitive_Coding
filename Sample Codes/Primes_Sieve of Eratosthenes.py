#Sieve of Eratosthenes
def SOE(n):
    primes = []
    val = [True for i in range(n+1)]
    val[0] = val[1] = False
    for ind in range(2,int(n**0.5)+1):
        if val[ind]:
            for x in range(ind**2,n+1,ind):
                val[x]=False
    for y in range(n+1):
        if val[y]:
            primes.append(y)
    return primes
