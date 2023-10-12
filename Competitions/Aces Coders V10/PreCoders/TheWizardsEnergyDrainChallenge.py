orb_1 = int(input())
orb_2 = int(input())

def count_ones(n):
    return str(bin(n)[2:]).count('1')

ans = -1

if orb_1 == 0 :
    ans = 0

elif orb_2==0:
    ans  = count_ones(orb_1)

elif orb_2>0:
    i = 1
    k = orb_1-i*orb_2
    while k>0:
        if count_ones(k)<=i<=k:
            ans = i
            break
        i += 1
        k = orb_1-i*orb_2

else:
    i = 1
    k = orb_1-i*orb_2
    while k>0:
        print(k,count_ones(k))
        if count_ones(k)<=i<=k:
            ans = i
            break
        i += 1
        k = orb_1-i*orb_2

print(ans)