devisors = [0]*(1000001)

for num in range(1,1000001):
    for i in range(0,1000001,num):
        devisors[i] += 1

for test in range(int(input())):
    print(devisors[int(input())])






# def SOE(n):
#     primes = []
#     val = [True for i in range(n+1)]
#     val[0] = val[1] = False
#     for ind in range(2,int(n**0.5)+1):
#         if val[ind]:
#             for x in range(ind**2,n+1,ind):
#                 val[x]=False
#     for y in range(n+1):
#         if val[y]:
#             primes.append(y)
#     return primes

# primes = SOE(5*10**5)

# for test in range(int(input())):
#     x = int(input())
#     i = 0
#     prime_factors = {}
#     while i < len(primes) and primes[i]<=x:
#         if x%primes[i]==0:
#             x = x//primes[i]
#             if primes[i] in prime_factors.keys():
#                 prime_factors[primes[i]] += 1
#             else:
#                 prime_factors[primes[i]] = 1
#         else:
#             i += 1
#     ans = 1
#     for value in prime_factors.values():
#         ans *= value+1

#     if ans == 1:
#         ans = 2

#     print(ans)
