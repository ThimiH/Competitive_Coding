s = input()
mod = 10**9+7
total = 0
prev = 0

for i,digit in enumerate(s):
    prev = (prev*10+int(digit)*(i+1))%mod
    total = (total+prev)%mod

print(total)