k = int(input())

prizelst = list(map(int,input().split(',')))

prizedict = {}

for i in range(len(prizelst)):
    try:
        prizedict[prizelst[i]].append(i)
    except:
        prizedict[prizelst[i]] = [i]

print(prizedict)
maxprof = 0

prizelst.sort()

def findpair(prizes):
    global prizedict
    global prizelst
    if len(prizes)==1:
        return 0
    pl = prizes[0]
    ph = prizes[-1]
    for plind in prizedict[pl]:
        for phind in prizedict[ph]:
            if plind<phind:
                prizedict[pl].remove(plind)
                prizedict[ph].remove(phind)
                prizelst.remove(pl)
                prizelst.remove(ph)
                print(pl,ph,'1')
                return ph-pl
    if checkpairlow(prizes) < checkpairhigh(prizes):
        return findpairhigh(prizes)
    else:
        return findpairlow(prizes)

def findpairlow(prizes):
    prizes = prizes[:-1]
    global prizedict
    global prizelst
    if len(prizes)==1:
        return 0
    pl = prizes[0]
    ph = prizes[-1]
    for plind in prizedict[pl]:
        for phind in prizedict[ph]:
            if plind<phind:
                prizedict[pl].remove(plind)
                prizedict[ph].remove(phind)
                prizelst.remove(pl)
                prizelst.remove(ph)
                print(pl,ph,'l')
                return ph-pl
    return findpairlow(prizes)

def findpairhigh(prizes):
    prizes = prizes[1:]
    global prizedict
    global prizelst
    if len(prizes)==1:
        return 0
    pl = prizes[0]
    ph = prizes[-1]
    for plind in prizedict[pl]:
        for phind in prizedict[ph]:
            if plind<phind:
                prizedict[pl].remove(plind)
                prizedict[ph].remove(phind)
                prizelst.remove(pl)
                prizelst.remove(ph)
                print(pl,ph,'h')
                return ph-pl
    return findpairhigh(prizes)

def checkpairlow(prizes):
    prizes = prizes[:-1]
    global prizedict
    global prizelst
    if len(prizes)==1:
        return 0
    pl = prizes[0]
    ph = prizes[-1]
    for plind in prizedict[pl]:
        for phind in prizedict[ph]:
            if plind<phind:
                return ph-pl
    return checkpairlow(prizes)

def checkpairhigh(prizes):
    prizes = prizes[1:]
    global prizedict
    global prizelst
    if len(prizes)==1:
        return 0
    pl = prizes[0]
    ph = prizes[-1]
    for plind in prizedict[pl]:
        for phind in prizedict[ph]:
            if plind<phind:
                return ph-pl
    return checkpairhigh(prizes)


for card in range(k):
    prof = findpair(prizelst)
    if prof == 0:
        break
    else:
        maxprof += prof

print(maxprof)