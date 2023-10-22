for test in range(int(input())):
    x_1,y_1,x_2,y_2,x_3,y_3 = tuple(map(int,input().split()))
    if x_1==x_2:
        if x_3 == x_1:
            print("TOUCH")
        elif x_3 <= x_1:
            print("LEFT")
        else:
            print("RIGHT")

    elif y_1 == y_2:
        if y_3 == y_1:
            print("TOUCH")
        elif y_3 <= y_1:
            print("LEFT")
        else:
            print("RIGHT")

    else:
        x_new = x_1 + (x_2-x_1)*(y_3-y_1)/(y_2-y_1)
        if float(x_3) == x_new:
            print("TOUCH")
        elif float(x_3) <= x_new:
            print("RIGHT")
        else:
            print("LEFT")