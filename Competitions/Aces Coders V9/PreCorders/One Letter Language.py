n = int(input())

answer = 0
for operation in range(n):
    operation = input()
    if operation == "--x" or operation == "x--":
        answer -= 1
    elif operation == "++x" or operation == "x++":
        answer += 1

print(answer)