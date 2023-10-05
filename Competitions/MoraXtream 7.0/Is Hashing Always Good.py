def hash(s,n,p):
    numb = 0
    for i in range(n):
        numb+=ord(s[i])*p[i]
    return numb%(10**n)

s = str(input())
n = len(s)
p = [5**x for x in range(n)]

count = 0

allstr = set({})

def allcases(stnow,prevs):
    le = len(stnow)
    global allstr
    if le==1:
        allstr.add(prevs+stnow)
    else:
        for i in range(le):
            allcases(stnow[:i]+stnow[i+1:],prevs+stnow[i])

q = allcases(s,'')

hashes = []

for item in allstr:
    new = hash(item,n,p)
    if new in hashes:
        count+=1
    else:
        hashes.append(new)

print(count)