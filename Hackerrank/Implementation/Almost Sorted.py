#Integer input
n = int(input())

#List input
unsrtlst = list(map(int,input().split()))

srtlst = unsrtlst.copy()

srtlst.sort()

for i in range(n):
    if unsrtlst[i]!=srtlst[i]:
        i1 = i
        break

for j in range(n-1,-1,-1):
    if unsrtlst[j]!=srtlst[j]:
        i2 = j
        break
if i2-i1==1:
    
    srl1 = unsrtlst[:i1]+[unsrtlst[i2]]+[unsrtlst[i1]]+unsrtlst[i2+1:]
else:
    srl1 = unsrtlst[:i1]+[unsrtlst[i2]]+unsrtlst[i1+1:i2]+[unsrtlst[i1]]+unsrtlst[i2+1:]
    
srl2 = unsrtlst[:i1]+unsrtlst[i1:i2+1][::-1]+unsrtlst[i2+1:]

if srtlst == srl1:
    print('yes')
    print('swap',i1+1,i2+1)
elif srtlst == srl2:
    print('yes')
    print('reverse',i1+1,i2+1)
else:
    print('no')