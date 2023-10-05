num = str(input())

index = 0
count = 0

if "1" not in num:
    print(-1)
else:
    while index < len(num):
        if num[index] == "0":
            index += 1
            countNew = 1
            while num[index%len(num)] == "0":
                countNew += 1
                index += 1
            count = max(count,countNew)
        else:
            index += 1

    print (count)