T = int(input())
Grid = []

for test_case in range(T):
    n = int(input())
    number_list = list(map(int,input().split()))
    if n == 1:
        print(number_list[0])
    elif n%2 == 1:
        answer = 0
        for index in range(0,n,2):
            answer = answer^number_list[index]
        print(answer)
    else:
        print(0)