




'''
def slicer(inlst):
    outlst = []
    for i in range(len(inlst)):
        outlst.append(inlst[:i]+inlst[i+1:])
    return outlst

def checker(inlst,sstr):
    l = len(inlst)
    checkin = sstr
    for let in inlst:
        if let in checkin:
            l-=1
            checkin = checkin[checkin.index(let)+1:]
            if l>len(checkin):
                return False
        else:
            return False
    return True

def stripfirst(lst1,lst2):
    rem1 = []
    rem2 = []

    for item in lst1:
        if item not in lst2:
            rem1.append(item)
    for item in lst2:
        if item not in lst1:
            rem2.append(item)

    for item in rem1:
        lst1.remove(item)
    for item in rem2:
        lst2.remove(item)

    return (lst1,lst2)

def goon(inlst):
    outlst = []
    for item in inlst:
        for newitem in slicer(item):
            if newitem not in outlst:
                outlst.append(newitem)
    return outlst

def commoncldbegin(lst1,lst2):
    l1 = len(lst1)
    l2 = len(lst2)
    if l1>l2:
        return (lst2,lst1,l2)
    else:
        return (lst1,lst2,l1)

s1 = list(input().strip())
s2 = list(input().strip())

s1,s2 = stripfirst(s1,s2)

s1,s2,ans = commoncldbegin(s1,s2)

checkin = [s1]
state = False

while True:
    for item in checkin:
        if checker(item,s2):
            state = True
    if state:
        break
    ans -=1
    checkin = goon(checkin)

print(ans)
'''