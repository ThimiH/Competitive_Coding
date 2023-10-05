N_a, N_b, N_c = tuple(map(int,input().split()))
X_a = list(map(int,input().split()))
X_b = list(map(int,input().split()))
X_c = list(map(int,input().split()))
q = int(input())
sizes = list(map(int,input().split()))

if N_a>N_b:
    if N_c>N_a:
        temp = X_b[:]
        X_b = X_a[:]
        X_a = temp[:]
    elif N_c<N_b :
        temp = X_c[:]
        X_c = X_a[:]
        X_a = temp[:]
    else:
        temp = X_b[:]
        X_b = X_c[:]
        X_c = temp[:]
else:
    if N_c<N_a:
        temp = X_b[:]
        X_b = X_a[:]
        X_a = X_c[:]
        X_c = temp[:]
    elif N_c<N_b:
        temp = X_b[:]
        X_b = X_c[:]
        X_c = temp[:]


counter_X_a = [0]*(8*10**4+1)
counter_X_b = [0]*(8*10**4+1)
counter_X_c = [0]*(8*10**4+1)

max_a = max_b = max_c = 0
min_a = min_b = min_c = float("INF")

for i in X_a:
    max_a = max(max_a,i)
    min_a = min(min_a,i)
    counter_X_a[i]+=1
for i in X_b:
    max_b = max(max_b,i)
    min_b = min(min_b,i)
    counter_X_b[i]+=1
for i in X_c:
    max_c = max(max_c,i)
    min_c = min(min_c,i)
    counter_X_c[i]+=1

count_X_a = {}
count_X_b = {}
count_X_c = {}

for i in range(min_a,max_a+1):
    if counter_X_a[i]!=0:
        count_X_a[i]=counter_X_a[i]

for i in range(min_b,max_b+1):
    if counter_X_b[i]!=0:
        count_X_b[i]=counter_X_b[i]

for i in range(min_c,max_c+1):
    if counter_X_c[i]!=0:
        count_X_c[i]=counter_X_c[i]

dp_b = [0]*(max_a+max_b+1)
dp_c = [0]*(10**5+1)

for ind_a,count_a in count_X_a.items():
    if ind_a>max_a:
        break
    for ind_b,count_b in count_X_b.items():
        if ind_b>max_b:
            break
        dp_b[ind_a+ind_b] += count_a*count_b

for ind_ab,count_ab in enumerate(dp_b):
    for ind_c,count_c in count_X_c.items():
        if ind_ab+ind_c>10**5:
            break
        dp_c[ind_ab+ind_c] += count_ab*count_c

for size in sizes:
    print(dp_c[size])