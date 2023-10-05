def checkPrime(num):
    for i in range(5,int(num**0.5)+2,2):
        if num%i==0:
            return False
    return True

Nlst=[]
primes = [2,3]
count = 2
testing = 1

T = int(input())
if 1<=T<=1000:
    for i in range(T):
        Nlst.append(int(input()))


if max(Nlst)<=10000 and min(Nlst)>=1:
    while count<=max(Nlst):
        val = testing*6
        if checkPrime(val-1):
            primes.append(val-1)
            count+=1
        if checkPrime(val+1):
            primes.append(val+1)
            count+=1
        testing+=1

    for val in Nlst:
        print(primes[val-1])