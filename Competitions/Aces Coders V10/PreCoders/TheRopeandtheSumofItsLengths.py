s = input()

ans = 0
l = len(s)

for i in range(l):
      if s[:l+1-i]==s[i:]:
        ans+=l-1

print(ans)