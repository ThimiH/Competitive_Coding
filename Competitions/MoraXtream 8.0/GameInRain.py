inp = input()
b,exp = int(inp[0]),inp[2:]

base_values = [b**i for i in range(20)]

def to_decimal(num):
    global base_values
    num = reversed(num)
    ans = 0
    for i in len(num):
        ans+=num[i]*base_values[i]
    return str(ans)

numbers = []
final = []
j = 0

# Incomplete