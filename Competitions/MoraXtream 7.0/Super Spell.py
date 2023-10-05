num = int(input())
mainlist = []

d = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,
            'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,
            'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,
            't':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    
di = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',
            8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',
            14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',
            20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}


if 1<= num <= 100:

    for i in range(num):
        ind = int(input())
        sublist = []
        if 1>ind or ind>1000 :
            break
        for x in range(ind):
            spell = str(input())
            sublist.append(spell)
        mainlist.append(sublist)

    if 1<=ind<=1000 :
        spelllist = []
        for lst in mainlist:
            indlist=[]
            for word in lst:
                wordind=[]
                for let in word:
                    wordind.append(d.get(let))
                wordind.sort()
                indlist.append(wordind[0])
            indlist.sort()
            spelllist.append(indlist)

        for indset in spelllist:
            superspell = ''.join(di.get(x) for x in indset)
            print(superspell)