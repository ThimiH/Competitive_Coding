Heroind = []
Sizelist = [1]

nums = str(input()).split()
N = int(nums[0])
K = int(nums[1])

for hero in range(N):
    Heroind.append(list(map(int,str(input()).split())))

Heroind.sort(key=lambda x: x[0])
print(Heroind)

Maxcount = int(N/K)

for i in range(Maxcount):
    for K in range(K,9):
        NOH = (i+1)*K
        for y in range(len(Heroind)-NOH+1):
            newset = Heroind[y:(y+NOH)]
            Klist = []
            print(newset)
            for item in newset:
                Klist.append(item[1])
                Kcount=[]
                for nums in range(1,9):
                    Kcount.append(Klist.count(nums))
                if Kcount.count((i+1))==K:
                    print(newset)
                    Sizelist.append(newset[-1][0]-newset[0][0])

Sizelist.sort()
print(Sizelist)
print(Sizelist[-1])


