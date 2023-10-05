a = input()
b = input()
mod = 10**9+7

anum = 0
bnum = 0
bsum = 0

for i in a:
    anum = (anum*2+int(i))%mod

for i in b:
    bnum = (bnum*2+int(i))%mod

for _ in range(314160):
    bsum = (bsum*2+bnum)%mod

print((anum^bsum)%mod)

