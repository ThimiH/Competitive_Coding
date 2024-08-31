s = input()

for i in range(len(s)-1):
    for j in range(len(s)-1):
        if s[j] == s[j+1]:
            s = s[:j]+s[j+2:]
            break

print(s if s else 'Empty String')