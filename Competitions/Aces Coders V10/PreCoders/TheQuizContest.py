for round in range(int(input())):
    a,b,c,d = tuple(map(int,input().split()))
    if a==0:
        print(1)
    elif a<abs(b-c):
        print(2*a+min(b,c)*2+1)
    elif a-max(b,c)+min(b,c)<d:
        print(a+b+c+a-max(b,c)+min(b,c)+1)
    else:
        print(a+b+c+d)