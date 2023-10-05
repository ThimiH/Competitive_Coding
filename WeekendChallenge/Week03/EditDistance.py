import sys
sys.setrecursionlimit(1000000)

a = input()
b = input()

if len(a)<len(b):
    c = a
    a = b
    b = c

def changes(a,b):
    if len(b) == 0:
        return len(a)
    if len(a)==len(b):
        if a[-1]==b[-1]:
            return changes(a[:-1],b[:-1])
        else:
            return 1+changes(a[:-1],b[:-1])
    else:
        if a[-1]==b[-1]:
            return changes(a[:-1],b[:-1])
        else:
            return 1 + min(changes(a[:-1],b[:-1]),changes(a[:-1],b))
        
print(changes(a,b))

        



# A = {}
# B = {}

# for i in range(ord('A'),ord('Z')+1):
#     A[chr(i)] = 0
#     B[chr(i)] = 0

# for let in a:
#     A[let]+=1
# for let in b:
#     B[let]+=1

# if len(a)>=len(b):
#     l = len(a)
#     ans = l
#     for i in range(ord('A'),ord('Z')+1):
#         ans -= max(0, A[chr(i)]-B[chr(i)])
# else:
#     l = len(b)
#     ans = l
#     for i in range(ord('A'),ord('Z')+1):
#         ans -= max(0, B[chr(i)]-A[chr(i)])

# print(ans)