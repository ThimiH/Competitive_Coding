def checkPrime(num):
    for i in range(5,int(num**0.5)+2,2):
        if num%i==0:
            return False
    return True

primefact= [2,3]

for i in range(5,40,2):
    if checkPrime(i):
        primefact.append(i)

anslist = [0,1]

for x in range(2,41):
    ans = anslist[-1]
    test = ans
    for p in primefact:
        if p>x:
            break
        while x%p==0:
            if test%p!=0:
                ans*=p
            else:
                test/=p
            x/=p
    anslist.append(ans)

T=int(input())
Nlst =[]

if 1<=T<=10:
    for i in range(T):
        Nlst.append(int(input()))

if (1<=min(Nlst)) and (max(Nlst)<=40):
    for item in Nlst:
        print(anslist[item])