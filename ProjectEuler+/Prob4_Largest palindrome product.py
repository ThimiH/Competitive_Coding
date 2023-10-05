allpal = []
for x in range(101,1000):
    for y in range(x,1000):
        number = x*y
        num = number
        if num>=101101:
            if num//100000==num%10:
                num = num%100000
                num = num//10
                if num//1000==num%10:
                    num = num%1000
                    num = num//10
                    if num//10==num%10:
                        allpal.append(number)

allpal.sort()

print(max(allpal))

T=int(input())
Nlst =[]

if 1<=T<=100:
    for i in range(T):
        Nlst.append(int(input()))

if (101101<min(Nlst)) and (max(Nlst)<1000000):
    for item in Nlst:
        for i in allpal:
            if i>=item:
                print(ans)
                break
            else:
                ans = i