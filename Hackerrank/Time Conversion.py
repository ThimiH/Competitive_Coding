timein = input()
h,m,s = timein[:-2].split(':')
if h == '12':
    if timein[-2:]=='AM':
        h = '00'
else:
    if timein[-2:]=='PM':
        h = str(int(h)+12)

print(h+':'+m+':'+s)