def checkPrime(num):
    for i in range(5,int(num**0.5)+2,2):
        if num%i==0:
            return False
    return True

Nlst=[]
primes = [2,3]
testing = 1

T = int(input())
if 1<=T<=10000:
    for i in range(T):
        Nlst.append(int(input()))

if max(Nlst)<=2000000 and min(Nlst)>=1:
    while primes[-1]<=max(Nlst):
        val = testing*6
        if checkPrime(val-1):
            primes.append(val-1)
        if checkPrime(val+1):
            primes.append(val+1)
        testing+=1

    for i in primes:
        if i == 2:
            totlist=[2]
        else:
            totlist.append(i+totlist[-1])

    for val in Nlst:
        for i in primes:
            if i>val:
                print(totlist[primes.index(i)-1])
                break