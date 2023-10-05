#Test cases
t = int(input()) 

for z in range(t):
    #Tuple input
    n,k = tuple(map(int,input().split()))

    if k == 0:
        print(*range(1,n+1),sep = ' ')

    elif n%(2*k)== 0:
        lst = []
        for i in range(n//(2*k)):
            for x in range(k):
                lst.append(2*k*i+k+1+x)
            for y in range(k):
                lst.append(2*k*i+1+y)
        print(* lst, sep = ' ')

    else:
        print(-1)

