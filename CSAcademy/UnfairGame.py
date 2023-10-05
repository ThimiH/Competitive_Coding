n = int(input())

nums = sorted(list(map(int,input().split())))

anslst = [0]

for i in nums[1:]:
    anslst[0]+=i

for ind in range(2,n-1,2):
    anslst.append(anslst[-1]-nums[ind])

print(max(anslst))