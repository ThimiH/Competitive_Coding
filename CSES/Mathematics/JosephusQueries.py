def number_removed(n,k):
    if n == 1 :
        return 1
    elif k<=(n+1)//2:
        if 2*k>n:
            return (2*k)%n
        else:
            return 2*k
    else:
        if n%2 == 1:
            return number_removed(n//2,k-(n+1)//2)*2+1
        else:
            return number_removed(n//2,k-(n+1)//2)*2-1
        
for test in range(int(input())):
    n,k = tuple(map(int,input().split()))
    print(number_removed(n,k))