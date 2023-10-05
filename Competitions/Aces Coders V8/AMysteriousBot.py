s = list(input())
s_first = s[:]
s_next = s[:]
l = len(s)
t = int(input())
for time in range(t):
    for i in range(l):
        if s[i]==s[(i+1)%l]:
            s_next[i]='L'
        elif (s[i]=='L' and s[(i+1)%l]=='O') or (s[i]=='E' and s[(i+1)%l]=='V') or (s[i]=='O' and s[(i+1)%l]=='L') or (s[i]=='V' and s[(i+1)%l]=='E'):
            s_next[i]='O'
        elif (s[i]=='L' and s[(i+1)%l]=='E') or (s[i]=='O' and s[(i+1)%l]=='V') or (s[i]=='E' and s[(i+1)%l]=='L') or (s[i]=='V' and s[(i+1)%l]=='O'):
            s_next[i]='E'
        else:
            s_next[i]='V'
    s = s_next[:]
    print(s)