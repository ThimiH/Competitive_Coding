from collections import defaultdict

strings = defaultdict(lambda: 0)

for _ in range(int(input())):
    strings[''.join(sorted(list(input())))]+=1

print(max(strings.values()))