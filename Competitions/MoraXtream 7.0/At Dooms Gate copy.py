item = [0,0,0,0,3,3,3,0,0,0]
total = 0
for i in item:
    total += i
    if i > 8:
        break
cnt=[]
for i in range(9):
    cnt.append(item.count(i+1))
cnt.sort()
print(cnt)
if total < 8 :
    print('rect')
elif item.count(1) > 2 :
    print('cross')
elif item.count(0) == 8 :
    if i == 8:
        if item.count(4) > 0:
            print('rect')
        else:
            print('tri')
    else:
        print('rect')
elif item.count(0) < 8 :
    if cnt[8]>2:
        print('rect')
    else: 
        print('tri')
else :
    if cnt[8]==2:
        print('rect')
    else:
        print('tri')