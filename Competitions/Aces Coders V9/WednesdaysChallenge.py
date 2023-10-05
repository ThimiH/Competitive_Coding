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

#binary search to find lowest values index in lst higher than or equal to val 
def binsearchup(lst,val):
    l = len(lst)
    a,b = 0,l
    while a+1!=b:
        i = (a+b)//2
        if lst[i]<=val:
            a = i
        else:
            b = i
    return b

k = 1.5*10**7
primelst = SOE(int(k))
checklst = []
for i in range(0,len(primelst),2):
    checklst.append(2*(i+1)*primelst[i])

t = int(input()) 

for z in range(t):
    #int input
    n = int(input())
    print(1+2*binsearchup(checklst,n))