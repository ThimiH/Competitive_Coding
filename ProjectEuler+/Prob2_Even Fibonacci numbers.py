def fib(n):
    fibos = [1,2]
    for i in range(n-2):
        fibos.append(fibos[-1]+fibos[-2])
    return fibos

def evenFib(n):
    fibos = fib(n)
    evenFibos = [2]
    evenFibosTotal = [2]
    for index in range(4,n,3):
        evenFibos.append(fibos[index])
        evenFibosTotal.append(evenFibosTotal[-1]+fibos[index])
    return(evenFibos,evenFibosTotal)

N = 100

evenFibos, evenFibosTotal = evenFib(N)

t  = int(input())

for testcase in range(t):
    n = int(input())
    for index in range(33)[::-1]:
        if evenFibos[index]<n:
            print(evenFibosTotal[index])
            break