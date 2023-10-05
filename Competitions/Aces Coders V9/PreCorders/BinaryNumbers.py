n = int(input())
mod = 10**9+7

powers = [2]
binn = bin(n)[2:]

powerSize = len(bin(n))-2

for _ in range(powerSize-1):
    powers.append(powers[-1]**2)

powers = powers[::-1]

answer = 1

for index in range(powerSize):
    if int(binn[index]):
        answer= (answer*powers[index])%mod

print(answer)

# PRIME = 10**9 + 7
# same_number = n // 30
# remaining = n % 30

# finals = []

# mod_now = 2**30 % PRIME

# while same_number>0:
#     if same_number%2:
#         finals.append(mod_now)
#     same_number = same_number//2
#     mod_now = (mod_now**2) % PRIME

# answer = 2**remaining

# for value in finals:
#     answer = (answer*value)%PRIME

# print(answer)