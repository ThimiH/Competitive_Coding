from bisect import insort_right

for test in range(int(input())):
    n = int(input())
    patients = []
    for i in range(1,n+1):
        l,r = tuple(map(int,input().split()))
        patients.append((i,l,r))
    patients.sort(key= lambda x : x[1])
    print(patients)
    nextup = []
    ans = []
    for j in range(1,n+1):
        while patients:
            if patients[0][1] == j:
                insort_right(nextup,patients.pop(0),key=lambda x: x[2])
            else:
                break
        print(nextup)
        i,l,r = nextup.pop(0)
        if r >= j:
            ans.append(i)
        else:
            break
    if len(ans) == n:
        print(*ans)
    else:
        print('impossible')
