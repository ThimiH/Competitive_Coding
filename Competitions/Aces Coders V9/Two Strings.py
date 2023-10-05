l1 = int(input())
string1 = str(input())
l2 = int(input())
string2 = str(input())

strdic1 = {}
strdic2 = {}

for l in string1:
    try:
        strdic1[l]+=1
    except:
        strdic1[l]=1

for l in string2:
    try:
        strdic2[l]+=1
    except:
        strdic2[l]=1

ans = 0

for a in strdic1.keys():
    try:
        ans += min(strdic1[a],strdic2[a])
    except:
        pass

print(ans)