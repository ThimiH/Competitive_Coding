oplst = []
oplst.append(input().split()[0])
ip = 0
while True:
    ipf = ip
    ip = input().split()[0]
    try:
        ip=int(ip)
    except:
        pass
    if ip == '#':
        break
    if ipf=='{+}' and ip == '{/+}':
        oplst = oplst[:-1]
    elif ipf=='{*}' and ip == '{/*}':
        oplst = oplst[:-1]
    elif ipf=='{-}' and ip == '{/-}':
        oplst = oplst[:-1]
    else:
        oplst.append(ip)

ind = 0
ops = []

while len(oplst)>3:
    if oplst[ind]=='{+}':
        ops.append([0,ind])
        currop = 0
        currind = ind+1
        ind+=1
    
    elif oplst[ind]=='{/+}':
        val = oplst[currind]
        ops= ops[:-1]
        oplst = oplst[:ind-2]+[val]+oplst[ind+1:]
        currop = ops[-1][0]
        currind = ops[-1][1]+1
        ind = currind
    
    elif oplst[ind]=='{-}':
        ops.append([1,ind])
        currop = 1
        currind = ind+1
        ind+=1
    
    elif oplst[ind]=='{/-}':
        val = oplst[currind]
        ops= ops[:-1]
        oplst = oplst[:ind-2]+[val]+oplst[ind+1:]
        currop = ops[-1][0]
        currind = ops[-1][1]+1
        ind = currind
    
    elif oplst[ind]=='{*}':
        ops.append([2,ind])
        currop = 2
        currind = ind+1
        ind+=1
    
    elif oplst[ind]=='{/*}':
        val = oplst[currind]
        ops= ops[:-1]
        oplst = oplst[:ind-2]+[val]+oplst[ind+1:]
        currop = ops[-1][0]
        currind = ops[-1][1]+1
        ind = currind
    
    else:
        if currop == 0:
            if ind == currind:
                ind += 1
            else:
                oplst[currind]+=oplst[ind]
                oplst = oplst[:ind]+oplst[ind+1:]
        elif currop == 1:
            if ind == currind:
                ind += 1
                pass
            else:
                oplst[currind]-=oplst[ind]
                oplst = oplst[:ind]+oplst[ind+1:]
        else:
            if ind == currind:
                ind += 1
                pass
            else:
                oplst[currind]*=oplst[ind]
                oplst = oplst[:ind]+oplst[ind+1:]

print(oplst[1]%(10**9+7))