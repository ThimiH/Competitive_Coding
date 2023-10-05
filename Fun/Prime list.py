N = 10**7+8
maxval = int(N**0.5)
index = 2

primes= [2,3] + list(range(5,N+1,6)) + list(range(7,N+1,6))
primes.sort()

def filter():
    global index
    global primes
    for i in primes[index+1:]:
        if i%primes[index]==0:
            primes.remove(i)
    index += 1
    if primes[index]<=maxval:
        filter()
    else:
        return None

filter()

print(len(primes), primes[-1])

