intstr = ''
for i in range(2500):
    intstr = intstr + str(i+1)

n = int(input())
if 1<n and n<10000:
    print(intstr[(n-1):n])
