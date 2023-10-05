n = int(input()) 
remlst = list(map(int,input().split()))
m = int(input()) 
orglst = list(map(int,input().split()))

first = [0]*10001
remain = [0]*10001
stolen = [0]*10001

for ind in range(n):
    remain[remlst[ind]]+=1

for ind in range(m):
    first[orglst[ind]]+=1

for ind in range(10001):
    stolen[ind]=first[ind]-remain[ind]
    if stolen[ind]:
        print(ind,end = " ")




# for item in remlst:
#     try:
#         orglst.remove(item)
#     except:
#         pass

# if n!=m:

#     orglst.sort()
#     orglst = list(set(orglst))

#     for plate in orglst:
#         print(plate, end=' ')