T=int(input())
Nlst =[]

if 1<=T<=10000:
    for i in range(T):
        Nlst.append(int(input()))

if (1<=min(Nlst)) and (max(Nlst)<=10000):
    for x in Nlst:
        print(int(x*(x*x-1)*(3*x+2)/12))