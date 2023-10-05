t = int(input())

for _ in range(t):
    n = int(input())
    values = list(map(int,input().split()))
    if len(values) == len(set(values)):
        print("First")
    else: 
        if n%2 == 0:
            print("Second")
        else:
            print("First")