A,B,C,D = tuple(map(int,input().split()))

subnum = []
for i in range(D):
    ip = str(input())
    if len(ip)<7 or ip == '1000000':
        subnum.append(ip)

numlst = [str(x) for x in range (A,B+1)]

def check (subs, num):
    for n in subs:
        if n in num:
            return False
    return True

rem = []

for number in numlst:
    if check(subnum,number):
        rem.append(number)
        if int(number)-A-len(rem)>C:
            break

for y in rem:
    numlst.remove(y)

try :
    print(numlst[C-1])

except:
    print('DOES NOT EXIST')