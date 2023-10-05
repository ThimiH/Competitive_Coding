num = int(input())

if 1<=num<=1000:
    inlist=[]
    for i in range(num):
        item = []
        for x in range(10):
            inp = input()
            if inp=='':
                item.append((input().split()).count('#'))
            else:
                item.append((inp.split()).count('#'))
        inlist.append(item)

    for square in inlist:
        total = 0
        for i in square:
            total += i
            if i > 8:
                break
        cnt=[]
        for i in range(9):
            cnt.append(square.count(i+1))
        cnt.sort()

        if total < 8 :
            print('rect')

        elif square.count(1) > 2 :
            print('cross')
        
        elif square.count(0) == 8 :
            if i == 8:
                if square.count(4) > 0:
                    print('rect')
                else:
                    print('tri')
            else:
                print('rect')
        
        elif square.count(0) < 8 :
            if cnt[8]>2:
                print('rect')

            else: 
                print('tri')
        
        else :
            if cnt[8]==2:
                print('rect')
            else:
                print('tri')