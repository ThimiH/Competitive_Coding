def Numfact(num):
    Ans=0
    sqr=num**0.5
    for i in range(1,int(sqr)+1):
        if num%i==0:
            Ans+=2
    if float(int(sqr))==sqr:
        return Ans-1
    else: 
        return Ans

def Nexttrig(trig,pos):
    return trig+pos+1

def filt(N):
    return None

triglst = [0]
poslst = [0]
factlst = [0]

T=int(input())
Nlst = []

if 1<=T<=10:
    for i in range(T):
        Nlst.append(int(input()))

if (1<=min(Nlst)) and (max(Nlst)<=1000):
    
    while factlst[-1]<=max(Nlst):
        triglst.append(Nexttrig(triglst[-1],poslst[-1]))
        poslst.append(poslst[-1]+1)
        factlst.append(Numfact(triglst[-1])) 
    
    for item in Nlst:
        ind = 0
        for num in factlst:
            if num>item:
                print(triglst[ind])
                break
            ind+=1