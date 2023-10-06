n = int(input())
numbers = list(map(int,input().split()))
numbers = sorted(numbers,reverse=True)

for divisor in range(max(numbers),0,-1):
    count = 0
    for number in numbers:
        if number < divisor:
            break
        if number%divisor == 0:
            count += 1
    if count>1:
        print(divisor)
        break 