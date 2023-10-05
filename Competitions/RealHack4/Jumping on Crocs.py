#Integer input
n = int(input()) 

#List input
inplst = list(map(int,input().split()))
inplst = inplst[1:]
moves = 0 

while len(inplst)>1:
    if inplst[1]==1:
        moves += 1
        inplst = inplst[1:]
    else :
        moves += 1
        inplst = inplst[2:]

if len(inplst)==1:
    print(moves+1)
else:
    print(moves)
