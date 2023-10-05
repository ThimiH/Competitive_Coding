num = int(input())
mins = []

for a in range(num):
    n = int(input())
    wd = str(input())
    chlst = [ord(x) for x in wd]
    mins.append(min(chlst))

mins.sort()

for let in mins:
    print(chr(let),end=' ')