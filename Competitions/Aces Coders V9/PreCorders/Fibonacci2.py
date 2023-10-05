cons = 10**9

def Mmul(M1,M2):
    a = M1[0][0]*M2[0][0]+M1[0][1]*M2[1][0]
    b = M1[0][0]*M2[0][1]+M1[0][1]*M2[1][1]
    c = M1[1][0]*M2[0][0]+M1[1][1]*M2[1][0]
    d = M1[1][0]*M2[0][1]+M1[1][1]*M2[1][1]
    return [[a%cons,b%cons],[c%cons,d%cons]]

M = [[[1,1],[1,0]]]
for i in range(60):
    M.append(Mmul(M[-1],M[-1]))

T = int(input())

if 0<T<=10:
    Nlst = []
    for val in range(T):
        Nlst.append(int(input()))

    if 40<=min(Nlst) and max(Nlst)<=10**18:
        for num in Nlst:
            bnum = bin(num-1)[2:]
            for i in range(1,len(bnum)+1):
                if bnum[-i] == '1':
                    try:
                        Mnew = Mmul(Mnew,M[i-1])
                    except:
                        Mnew = M[i-1]
            print(Mnew[0][0])
            del(Mnew)