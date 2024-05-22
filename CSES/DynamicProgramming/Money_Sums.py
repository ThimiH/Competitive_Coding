from collections import defaultdict

n = int(input())
coins = sorted(list(map(int, input().split())))

possible = defaultdict(lambda: True)
possible[coins[0]]

for coin in coins[1:]:
    for sum in list(possible.keys()):
        possible[sum + coin]
    possible[coin]

print(len(possible))
print(*sorted(list(possible.keys())))