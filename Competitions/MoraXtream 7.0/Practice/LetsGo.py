n = int(input())

if 2<=n and n<=20:
    for _ in range(n-1):
        print(" ", end = "")
        for _ in range(n-1):
            print(" *", end = "")
        print()

    for row in range(n+1):
        print(" "*row, end = "")
        for _ in range(n-row):
            print("* ", end = "")
        print("*")