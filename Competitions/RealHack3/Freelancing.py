t,n = tuple(map(int,input().split()))

data = []
for _ in range(n):
    job, time_taken, payment = input().split()
    data.append([job,int(time_taken),int(payment)])

def custom_sort(sublist):
    return (sublist[1],-sublist[2])

sorted_data = sorted(data, key=custom_sort)

time = 0
ans = 0

for job in sorted_data:
    time += job[1]
    if time > t:
        break
    ans += job[2]

print(ans)