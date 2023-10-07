s = input()

letter_count =  {}

for num in range(ord("a"),ord("z")+1):
    letter_count[num] = 0

n = len(s)

for letter in s:
    letter_count[ord(letter)]+=1

MOD = 10**9+7

fact_n = 1

for i in range(1,n+1):
    fact_n = (fact_n*i)%MOD

MMI = [1]


for i in range(1,max(letter_count.values())+1):
    MMI.append((MMI[-1]*pow(i,MOD-2,MOD))%MOD)

ans = fact_n

for value in letter_count.values():
    ans = (ans*MMI[value])%MOD

print(ans)