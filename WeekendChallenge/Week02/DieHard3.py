import math

for test in range(int(input())):
    a,b,c = tuple(map(int,input().split()))
    if a>c or b>c:
        if c%math.gcd(a,b)==0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
