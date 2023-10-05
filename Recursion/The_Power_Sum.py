X = int(input())
N = int(input())

ans = 0

def findComb(n,i,N):
    if n-(i**N) == 0:
        global ans
        ans += 1
        return None
    if n-(i**N) > 0:
        findComb(n-(i**N),i+1,N)
        findComb(n,i+1,N)

findComb(X,1,N)

print(ans)