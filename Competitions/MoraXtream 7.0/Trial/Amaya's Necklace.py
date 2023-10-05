opattern = str(input())

def check2(opattern,indexlist,pattern):
    patternnow=[]
    for x in indexlist:
        patternnow.append(opattern[x])

    for item in pattern:
        try:
            ind = patternnow.index(item)+1
            patternnow = patternnow[ind:]

        except:
            return False
    
    return True


def check(opattern,indexlist,pattern):
    
    patternnow=[]
    for x in indexlist:
        patternnow.append(opattern[x])
        
    while True:
        if patternnow[0] == pattern[0]:
            patternnow.pop(0)
            pattern.pop(0)
        else :
            patternnow.pop(0)

        if len(patternnow) == 0 or len(pattern) == 0:
            break 

    if pattern == []:
        return True
    else :
        return False

if 5<len(opattern)<100000:
    pat = str(input())
    order = str(input())
    orderlist = order.split()

    if len(opattern) == len(orderlist):
        pattern = [i for i in pat]
        outint = 0

        indexlist = list(range(len(opattern)))

        for item in orderlist:
            try:
                indexlist.remove(int(item)-1)
            except:
                None
            
            pattern = [i for i in pat]
            if check2(opattern,indexlist,pattern):
                outint += 1
            else :
                print(outint)
                break
            if len(indexlist) == len(pattern):
                print(outint)
                break