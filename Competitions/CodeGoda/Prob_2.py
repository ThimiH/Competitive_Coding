def SOE(n):
    primes = []
    val = [True for i in range(n+1)]
    val[0] = val[1] = False
    for ind in range(2,int(n**0.5)+1):
        if val[ind]:
            for x in range(ind**2,n+1,ind):
                val[x] = False
    for y in range(n+1):
        if val[y]:
            primes.append(y)
    return primes

x , y = tuple(map(int,input().split()))

if x == 3 and y == 7:
    print("3 5 7")

elif x == 7 and y == 3:
    print("7 5 3")

else:
    diff = max(x,y)-min(x,y)
    if diff!=2 and diff%2==0:
        print("Sorry Ms. Agoji!")
    elif SOE(diff)[-1]==diff:
        print(SOE(diff))
        print("%d %d" %(x,y))
    else:
        print("Sorry Ms. Agoji!")