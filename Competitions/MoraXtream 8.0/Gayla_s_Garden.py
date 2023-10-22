n,k = tuple(map(int,input().split()))
lst = sorted(list(set(map(int,input().split()))))
n = len(lst)

ans1 = 0
plant = 0

while plant<n:
    thr = lst[plant]+k
    while lst[plant]<thr:
        plant+=1
        if plant==n:
            break
    plant-=1
    ans1+=1
    thr = lst[plant]+k
    while lst[plant]<thr:
        plant+=1
        if plant==n:
            break

lst = lst[::-1]
ans2 = 0
plant = 0

while plant<n:
    thr = lst[plant]+k
    while lst[plant]<thr:
        plant+=1
        if plant==n:
            break
    plant-=1
    ans2+=1
    thr = lst[plant]+k
    while lst[plant]<thr:
        plant+=1
        if plant==n:
            break

print(min(ans1,ans2))
    

    