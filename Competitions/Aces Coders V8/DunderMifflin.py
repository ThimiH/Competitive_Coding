def roomNum(x,y):
    n = x+y
    prev = (n*(n+1)//2)
    numb = prev + x
    return numb

t = int(input())

for _ in range(t):
    x,y = tuple(map(int,input().split()))
    print("C"+str(roomNum(x,y)))