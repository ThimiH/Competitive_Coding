n,k = tuple(map(int,input().split()))
stri = str(input())

cngmust = 0
couples = []

if n%2 == 0:
    for i in range(n//2):
        couples.append([stri[i],stri[n-i-1]])
        if stri[i]==stri[n-i-1]:
            pass
        else:
            cngmust+=1
else:
    for i in range(n//2):
        couples.append([stri[i],stri[n-i-1]])
        if stri[i]==stri[n-i-1]:
            pass
        else:
            cngmust+=1
    couples.append([stri[n//2]])

if cngmust > k:
    print(-1)
else:
    for i in range(len(couples)):
        if couples[i][0]!=couples[i][-1]:
            couples[i][0]=couples[i][-1]=max(couples[i][0],couples[i][-1])

    rem = k - cngmust
    renewed = 0
    while renewed <= rem:
        

    print(couples)