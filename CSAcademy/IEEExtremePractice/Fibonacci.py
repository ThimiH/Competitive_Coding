def fibonacci(n,MOD):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if n%2 == 0:
            return (2*fibonacci(n//2-1,MOD)*fibonacci(n//2,MOD)+fibonacci(n//2,MOD)**2)%MOD
        else:
            return (fibonacci(n//2,MOD)**2+fibonacci(n//2+1,MOD)**2)%MOD
        
for test in range(int(input())):
    n = int(input())
    print(fibonacci(n+1,10))