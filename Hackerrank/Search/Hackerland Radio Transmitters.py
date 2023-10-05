#Tuple input
n,k = tuple(map(int,input().split()))

#List input
xlst = list(map(int,input().split()))
xlst.sort()

start = 0
even = 0
i = 0

while i<n:
    if xlst[i]-xlst[start]>k:
        even += 1
        if even%2==0:
            start = i
        else:
            start = i-1
            i-=1
    i += 1

print (even//2+1)