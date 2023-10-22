def powerSum(x,n,i):
    if x == i**n:
        return 1
    elif x < i**n:
        return 0
    else:
        return powerSum(x-i**n,n,i+1)+powerSum(x,n,i+1)
    
x = int(input())
n = int(input())

print(powerSum(x,n,1))