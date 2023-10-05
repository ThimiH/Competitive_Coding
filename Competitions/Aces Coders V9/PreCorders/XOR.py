'''t = int(input())
sizelst=[]

if 1<=t<=5:
    for i in range(t):
        sis = int(input())
        elm = list(map(int, input().split()))
        if len(elm)==sis and (2<=sis<=10**5):
            sublst = []
            for x in range(len(elm)):
                for y in range (len(elm)-x):
                    sublst.append(elm[y:y+x+1])

            intlst = []

            for item in sublst:
                if len(item)==1:
                    intlst.append(item[0])
                else:
                    xor = []
                    for y in item:
                        if xor == []:
                            xor = y
                        else:
                            xor = xor^y
                    
                    intlst.append(int(xor))

            xor = 'b'
            for y in intlst:
                if xor == []:
                    xor = y
                else:
                    xor = xor^y
        
            sizelst.append(int(xor))




for item in sizelst:
    print(item)
'''

T = int(input())
Nlst = []
Grid = []

def Check(Grid):
    for a in Grid:
        for b in a:
            if 1<=b<=10**8:
                continue
            else:
                return False
    return True

if 1<=T<=5:
    for x in range(T):
        Nlst.append(int(input()))
        Grid.append(list(map(int,input().split())))

    if 1<=min(Nlst) and max(Nlst)<=10**5:
        if Check(Grid):
            for y in range(T):
                if Nlst[y] == 1:
                    print(Grid[y][0])
                elif Nlst[y]%2!=0:
                    ans = 0
                    for val in range(0,Nlst[y],2): 
                        ans=ans^Grid[y][val]
                    print(ans)
                else:
                    print(0)
