mod = 10**9+7

combinations = [[0]*10]
for _ in range(9):
    combinations.append([1]*10)

def update(grid):
    global mod
    newGrid = [[0]*10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if i+j<10:
                for k in range(10-(i+j)):
                    newGrid[j][k] += (grid[i][j]%mod)
    return newGrid

n = int(input())

for _ in range(n-2):
    combinations = update(combinations)

ans = 0

for i in range(10):
    for j in range(10):
        ans += combinations[i][j]

print(ans)