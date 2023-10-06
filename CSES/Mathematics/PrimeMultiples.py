from sys import setrecursionlimit

n,k = tuple(map(int,input().split()))
primes = list(map(int,input().split()))

setrecursionlimit(2**k)

intersections = [[] for _ in range(k)]

def intersection_find(index,n,elements):
    global primes
    global intersections
    if index == -1 or n == 0:
        return None
    else:
        intersections[elements].append(n//primes[index])
        intersection_find(index-1,n//primes[index],elements+1)
        intersection_find(index-1,n,elements)

intersection_find(k-1,n,0)

ans = 0

for i in range(k):
    if i%2==0:
        for num in intersections[i]:
            ans += num
    else:
        for num in intersections[i]:
            ans -= num

print(ans)