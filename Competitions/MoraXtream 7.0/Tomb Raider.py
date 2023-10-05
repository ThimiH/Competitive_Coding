t = int(input())

for testcase in range(t):
    answer = True
    n = int(input())
    number = input()
    length = len(number)
    configurations = [1 for index in range(length)]
    for index in range(1,length):
        configurations[index] = configurations[index-1]
        if number[index]=='0':
            if not int(number[index-1:index+1])<=n:
                answer = False
        if int(number[index-1:index+1])<=n:
            configurations[index] += configurations[index-2]
    if answer:
        print(configurations[-1])
    else:
        print(0)
