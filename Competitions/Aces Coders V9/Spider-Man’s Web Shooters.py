n = int(input())
lst = list(set(map(int,input().split())))

minimum = float("INF")
maximum = 0

for i in lst:
    maximum = max(maximum,i)
    minimum = min(minimum,i)

size = maximum+1-minimum
available = [0]*(size)
gaps = 0

for i in lst:
    available[i-minimum] = 1

for gap in range(1,size):
    for i in range(size-1):
        if available[i] and available[i+gap]:
            gaps+=1
            break

print(gaps)

# dset = set()

# for i in range(len(lst-1)):
#     house = lst[i]
#     for bu in lst[i+1:]:
#         dset.add(abs(bu-house))

# print(len(dset))