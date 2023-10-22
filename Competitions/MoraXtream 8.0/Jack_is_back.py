from collections import defaultdict
n = int(input())
boxes = []
for _ in range(n):
    boxes.append(input())

mat = defaultdict(lambda : 0)
m = 0

for i in range(n):
    for j in range(i):
        s = set(boxes[i]+boxes[j])
        m = max(m,max(map(int,s)))
        mat[len(s)]+=1

print("%.2f" %(mat[m+1]*2/n/(n-1)))