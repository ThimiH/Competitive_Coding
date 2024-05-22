from collections import defaultdict
from bisect import bisect_left

position = defaultdict(lambda : [])

s = input()
for i,l in enumerate(s):
    position[ord(l)].append(i)

for _ in range(int(input())):
    q = input()
    answer = 0
    index = i+1
    for letter in q[::-1]:
        p = bisect_left(position[ord(letter)],index)
        if p and position[ord(letter)]:
            index = position[ord(letter)][p-1]
            answer += 1
        else:
            break
    print(answer)