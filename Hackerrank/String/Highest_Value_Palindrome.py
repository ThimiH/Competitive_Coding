n,k = map(int, input().split()) 
s = input()
if n%2:
    left = list(s[:n//2])
    right = list(s[n//2+1:][::-1])

    mid = s[n//2]
else:
    left = list(s[:n//2])
    right = list(s[n//2:][::-1])
    mid = ''

edited = [False]*(n//2)

for i in range(n//2):
    if k == 0:
        break
    if left[i] != right[i]:
        if int(left[i]) > int(right[i]):
            right[i] = left[i]
        else:
            left[i] = right[i]
        edited[i] = True
        k -= 1

for i in range(n//2):
    if k == 0:
        break
    if left[i] != '9':
        if edited[i]:
            k += 1
        if k >= 2:
            left[i] = '9'
            right[i] = '9'
            k -= 2
        elif k == 1 and edited[i]:
            k -= 1

if k > 0 and mid:
    mid = '9'

if left == right:
    print(''.join(left)+mid+''.join(right[::-1]))
else:
    print(-1) 
        