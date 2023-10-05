n = int(input())
ans = 0
for z in range(n):
    ans += int(input())

print(str(ans)[:10])


'''n = int(input())
nums = []
for z in range(n):
    nums.append(str(input()))

def adder(num, ind):
    global n
    global nums
    ans = num*10
    for m in range(n):
        ans += int(nums[m][ind])
    return ans

a1 = 0
a2 = 1
p = 0

while str(a1)[:10]!=str(a2)[:10] or p<n:
    a1 = adder(a1,p)
    p += 1
    a2 = a1 + 9*n
    print(a1)

print(str(a1)[:10])
'''