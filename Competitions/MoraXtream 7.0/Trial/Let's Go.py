while True:
    try:
        n=int(input())
    except:
        break

    if 2>n or n>20:
        break
        
    sp = ' '
    st = '*'
    row = ''

    spst = sp+st
    for i in range(n-1):
        row = row + spst

    row = sp + row

    for i in range(n-1):
        print(row)

    for i in range(n+1):
        row = sp*i + st
        for x in range(n-i):
            row = row + spst
        print(row)    