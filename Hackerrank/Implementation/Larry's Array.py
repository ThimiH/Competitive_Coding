t = int(input()) 

for z in range(t):
    #int input
    n = int(input()) 

    #List input
    indlst = list(map(int,input().split()))
    val = 0
    for ind in range(n):
        val += indlst[ind]-ind

    if val == n:
        print ('YES')

    else:
        print('NO')