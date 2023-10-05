n = int(input())

nums = list(map(int,input().split()))

n = nums[0]

right = []

for num in nums[1:]:
    if num<n:
        print(num, end=" ")
    if num>n:
        right.append(num)

print(n, end = " ")

for num in right:
    print(num, end=" ")